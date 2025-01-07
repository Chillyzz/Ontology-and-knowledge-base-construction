import transformers
import torch
import json
import re
from compute_similarity import find_top_k
from find_ops import extract_ops, find_ops_in_text
from openai import OpenAI

instruction = "You are a professional translator who is good at translating natural language text into assertion logic expressions. I will provide you with relevant knowledge of assertion logic 'K', 3 translation examples, a natural language text to be translated 'T', and a list of candidate assertion logic functions 'F'. Your task is to select the functions required to translate the text 'T' from the candidate list 'F' and return them in the form of a list."

assertion_knowledge = '''
Assertion Logic Knowledge 'K':
The expression of assertion logic is defined as follows:
1. Assertion logic consists of declarations, facts and query targets
2. The form of declaration is variable_name:type, where variable_name is the variable name and type is the variable type.
3. The type of fact is expr_lhs = expr_rhs, where expr is any expression.
4. Expressions consist of variables, constants or functions acting on variables, similar to programming languages, and can be nested.
5. The query target is an expression, which means that given all declarations and assertions, the value of this target needs to be queried.
6. During the translation process, you need to pay attention to the consistency of the variables you use, and you cannot declare more or less variables.
7. All variable types and a list of candidate functions are given below. Be careful not to use variable types or functions that are not shown below.

*************** Type list ***************
1. Curve: Curve
2. ConicSection \\in Curve: Conic section
3. Line \\in Curve: Line
4. LineSegment \\in Curve: Line segment
5. Ray \\in Curve: Ray
6. Hyperbola \\in ConicSection: Hyperbola
7. Circle \\in ConicSection: Circle
8. Parabola \\in ConicSection: Parabola
9. Ellipse \\in ConicSection: Ellipse
10. Point: Point in a two-dimensional coordinate system
11. Origin \\in Point: Origin of a two-dimensional coordinate system
12. axis: Coordinate axis in a two-dimensional coordinate system
13. xAxis \\in axis: Horizontal coordinate in a two-dimensional coordinate system
14. yAxis \\in axis: Vertical coordinate in a two-dimensional coordinate system
15. Vector: Two-dimensional vector
16. Angle: Angle
17. Number: Number
18. Real \\in Number: Real number
19. rad: radian
20. degree: degree
21. pi: pi
22. pm: ±

*************** Candidate Functions list 'F' ***************
{}

'''

few_shots = '''
Example {}:
Natural Language Text 'T':
{}

Functions Required To Translate:
{}
'''

answer_template = '''
Natural Language Text 'T':
{}

Functions Required To Translate:
'''


def extract_parts(input_text, patterns):
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, input_text, re.DOTALL)
        if match:
            # 去掉内容中的多余空格和换行符
            result[key] = " ".join(match.group(1).strip().split())
    return result


def main():
    client = OpenAI(api_key="sk-9572711a6c854dcd94ab3b93c2276bb5", base_url="https://api.deepseek.com")

    train_f = r'/home/zcl/conic10k/conic10k/top_200_rich_datas_cluster_with_text.json'
    test_f = r'/home/zcl/conic10k/new_data/test_300_breakdown.json'
    output = r'/home/zcl/conic10k/Few-shot/text_300_filter_ops.json'

    operators_file = open('/home/zcl/conic10k/Few-shot/operators.json','r',encoding='utf-8')
    operators = json.load(operators_file)

    test = open(test_f,'r',encoding='utf-8')
    train = open(train_f,'r',encoding='utf-8')
    f1 = open(output,'a',encoding='utf-8')

    test_datas = json.load(test)
    train_datas = json.load(train)
    answers = []
    
    for j, data in enumerate(test_datas):
        # if 0 <= j < 100:
            d = dict()
            question = data['text']
            new_question = data['new_text']
            # 寻找前3个shot
            sim_res = find_top_k(question,train_datas,3)
            sim_text = []
            all_ops = []
            all_ops.extend(find_ops_in_text(question))
            for i,res in enumerate(sim_res):
                text = res['text']
                new_text = res['new_text']
                declarations = res['declarations']
                facts = res['facts']
                query = res['query']
                input_shot = few_shots.format(i+1, new_text, extract_ops(text, declarations, facts, query))
                sim_text.append(input_shot)
                all_ops.extend(extract_ops(text,declarations,facts,query))

            final_shot_prompt = '\n'.join(sim_text)
        
            # 选取operator
            # all_ops.extend(['Coordinate','Negation','ApplyUnit','Range','Abs','OneOf'])
            operators_prompt = []
            for index,op in enumerate(set(all_ops)):
                op_prompt = f'{index+1}. {operators[op]}'
                operators_prompt.append(op_prompt)
            final_op_prompt = '\n'.join(operators_prompt)
            final_assertion_knowledge = assertion_knowledge.format(final_op_prompt)

            final_input = final_assertion_knowledge + final_shot_prompt + answer_template.format(new_question)

            # print(final_input)
            # breakpoint()

            response = client.chat.completions.create(
                model="deepseek-coder",
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": final_input},
                ],
                stream=False
            )
            d['text'] = question
            d['new_text'] = new_question
            d['init_ops'] = all_ops
            ans = response.choices[0].message.content
            d['filter_ops'] = ans

            print(f'问题：\n{question}\n\n')
            print(f"回答：\n{ans}\n\n")

            json.dump(d,f1,ensure_ascii=False,indent=4)
            f1.write(',\n')
            f1.flush()
        

if __name__ == "__main__":
    main()