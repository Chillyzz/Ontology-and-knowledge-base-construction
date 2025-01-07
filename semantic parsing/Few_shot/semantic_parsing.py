import transformers
import torch
import json
import re

from process_data.compute_similarity import find_top_k

from openai import OpenAI

instruction = "You are a professional translator who is good at translating natural language into various forms of language. When I provide you with a text, assertion logic knowledge, and 5 translation examples, your task is to master the assertion logic knowledge and translate the text into the corresponding assertion logic expression."

assertion_knowledge = '''
Assertion Logic Knowledge:
1. Assertion logic consists of declarations, facts and query targets
2. The form of declaration is variable_name:type, where variable_name is the variable name and type is the variable type.
3. The type of fact is expr_lhs = expr_rhs, where expr is any expression.
4. Expressions consist of variables, constants or functions acting on variables, similar to programming languages, and can be nested.

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

*************** Function List ***************
{}
'''

few_shots = '''
Translation Example {}:
Text:
{}

Translation Result:
```
Declarations: {}
Facts: {}
Query: {}
```
'''

answer_template = '''
Text:
{}

Translation Result:'''


def extract_parts(input_text, patterns):
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, input_text, re.DOTALL)
        if match:
            # 去掉内容中的多余空格和换行符
            result[key] = " ".join(match.group(1).strip().split())
    return result


def main():
    client = OpenAI(api_key="xxx", base_url="https://api.deepseek.com")

    train_f = r'/home/zcl/conic10k/conic10k/top_200_break_down_sentences.json'  # 候选池数据
    test_f = r'/home/zcl/conic10k/conic10k/top_300_test_with_new_text_process.json' # 测试数据
    output = r'/home/zcl/conic10k/Refine/few_shot/deepseek_breakdown_res_Jaro_Match_Distance.json' # 输出文件

    test = open(test_f,'r',encoding='utf-8')
    train = open(train_f,'r',encoding='utf-8')
    f1 = open(output,'a',encoding='utf-8')

    text_to_ops_file = open('/home/zcl/conic10k/Few_shot/text_to_ops.json','r',encoding='utf-8')
    text_to_ops = json.load(text_to_ops_file)

    operators_file = open('/home/zcl/conic10k/Few_shot/operators.json','r',encoding='utf-8')
    all_operators = json.load(operators_file)

    test_datas = json.load(test)
    train_datas = json.load(train)
    answers = []
    
    for j, data in enumerate(test_datas):
        # if j > 98:
            d = dict()
            question = data['text']
            new_question = data['new_text']
            d['text'] = question
            d['new_text'] = new_question
            d['ans'] = []
            
            for sentence in new_question:
                candidate_ops = []
                shots = []
                # 寻找前5个shot
                sim_res = find_top_k(sentence,train_datas,5)
                for i,res in enumerate(sim_res):
                    text = res['text']
                    ops = res['ops'] 
                    expressions = res['expression'].split('; ')
                    candidate_ops.extend(ops)
                    declaration = []
                    fact = []
                    query = []
                    for expression in expressions:
                        if ':' in expression:
                            declaration.append(expression)
                        elif '?' in expression:
                            query.append(expression)
                        else:
                            fact.append(expression)
                    few_shot = few_shots.format(str(i), text, declaration, fact, query)
                    shots.append(few_shot)

                final_shot_prompt = '\n'.join(shots)
            
                # 选取operator
                for t in text_to_ops.keys():
                    if t in sentence:
                        candidate_ops.extend(text_to_ops[t])
                final_all_ops = []
                candidate_ops = set(candidate_ops)
                for i,op in enumerate(candidate_ops):
                    final_all_ops.append(f'{i+1}. {all_operators[op]}')
                final_ops_prompt = '\n'.join(final_all_ops)

                final_input = assertion_knowledge.format(final_ops_prompt) + '\n' + final_shot_prompt + '\n' + answer_template.format(sentence)
                
                # print(instruction + '\n' + final_input)
                # breakpoint()

                response = client.chat.completions.create(
                    model="deepseek-coder",
                    messages=[
                        {"role": "system", "content": instruction},
                        {"role": "user", "content": final_input},
                    ],
                    stream=False
                )

                ans = response.choices[0].message.content
                d['ans'].append(ans)

                print(f"\n\n问题：\n{sentence}\n\n")
                print(f"\n\n回答：\n{ans}\n\n")

            json.dump(d,f1,ensure_ascii=False,indent=4)
            f1.write(',\n')
            f1.flush()
        

if __name__ == "__main__":
    main()