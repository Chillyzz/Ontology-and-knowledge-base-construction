import json
import re
from openai import OpenAI
import difflib
import json
import heapq

instruction = "You are a professional translator who is good at translating assertion logic into lean language. When I provide you with knowledge about assertion logic, the conversion rules from assertion logic to lean, and some translation examples, your task is to master the translation skills and translate the assertion logic expressions into the corresponding lean expressions."

Al_2_Lean_Rules = '''
****** Rule {} ******
Assertional_Logic: {}
Lean4_Code: {}
Explanation: {}
'''

shots_template = '''
###### Example {} ######
ID: {}
Declarations: {}
Facts: {}
Query: {}
Proof: {}

Lean Result: {}
'''

answer_template = '''
Now please translate the following assertion logic into lean.
Declarations: {}
Facts: {}
Query: {}
Proof: {}

Lean Result:
'''

def extract_concepts(declarations):
    all_concepts = []
    semantics = declarations.split(';')
    for semantic in semantics:
        if ':' in semantic:
            all_concepts.append(semantic.split(': ')[-1].split(' ')[0].strip())
    return list(set(all_concepts))

def extract_operators(facts):
    all_operators = []
    semantics = facts.split(';')
    for semantic in semantics:
        pattern = r"(?<=[^a-zA-Z_])([a-zA-Z_]+)(?=\()"
        matches = re.findall(pattern, semantic)
        all_operators.extend(matches)
    return list(set(all_operators))


def build_al_2_lean_prompt(concepts, operators):
    res_shot = []
    i = 1
    for concept in concepts:
        for data in al_2_lean_concepts:
            if data["Assertional_Logic"].lower() == concept.lower():
                res_shot.append(Al_2_Lean_Rules.format(str(i), data["Assertional_Logic"], data["Lean4_Code"], data["Explanation"]))
                i += 1
    for operator in operators:
        for data in al_2_lean_operators:
            if data["Assertional_Logic"].split('(')[0].strip().lower() == operator.lower():
                res_shot.append(Al_2_Lean_Rules.format(str(i), data["Assertional_Logic"], data["Lean4_Code"], data["Explanation"]))
                i += 1
    return '\n'.join(res_shot)


def match_ratio(text,datas):
    similaritys = []
    for data in datas:
        similaritys.append(difflib.SequenceMatcher(None,text,data).quick_ratio())
    return similaritys

def find_top_k(al,train_datas,k):
    datas = []
    for data in train_datas:
        declarations = data["Declarations"]
        facts = data["Facts"]
        query = data["Query"]
        proof = data['Proof']
        datas.append(declarations + '; ' + facts + '; ' + query + '; ' + proof)
        
    # res_1 = JaroDistance(text, datas)
    res_2 = match_ratio(al, datas)
    # largest_k_1 = heapq.nlargest(k,res_1)
    largest_k_2 = heapq.nlargest(k,res_2)

    result = []
    # for index,value in enumerate(res_1):
    #     if value in largest_k_1:
    #         result.append(train_datas[index])
    for index,value in enumerate(res_2):
        if value in largest_k_2:
            result.append(train_datas[index])
    return result


def find_shots(al, shots_data, k=3):
    few_shots = find_top_k(al, shots_data, k)
    few_shots_prompt = []
    question_concepts = []
    question_operators = []
    # 提取算子和概念
    for i,shot in enumerate(few_shots):
        declarations = shot['Declarations']
        facts = shot['Facts']
        query = shot['Query']
        proof = shot['Proof']
        lean = shot["lean"]
        semantics = declarations + '; '+ facts + '; '+ query + '; ' + proof
        question_concepts.extend(extract_concepts(semantics))
        question_operators.extend(extract_operators(semantics))
        few_shots_prompt.append(shots_template.format(str(i+1), shot["id"], declarations, facts, query, proof, lean))
    return few_shots_prompt, question_concepts, question_operators


operators_file = open(r'D:\桌面\6023\k12\MATH\operators.json','r',encoding='utf-8')
operators_data = json.load(operators_file)

concepts_file = open(r'D:\桌面\6023\k12\MATH\concepts.json','r',encoding='utf-8')
concepts_data = json.load(concepts_file)

# al到lean的规则
al_2_lean_concepts = json.load(open(r'AL-Lean4-Concept.json','r',encoding='utf-8'))     
al_2_lean_operators = json.load(open(r'AL-Lean4-Operator.json','r',encoding='utf-8'))

def main():
    client = OpenAI(api_key="", base_url="https://ark.cn-beijing.volces.com/api/v3")

    train_f = r'Al_Lean4_pools.json'   # 标注样例
    test_f = r''      # 测试数据
    output = r'test_result.json'

    test = open(test_f,'r',encoding='utf-8')
    train = open(train_f,'r',encoding='utf-8')
    f1 = open(output,'a',encoding='utf-8')

    test_datas = json.load(test)
    train_datas = json.load(train)

    test_time = []

    for j, data in enumerate(test_datas):
        # if j >= 198:
            d = dict()
            declaration = data["Declarations"]
            facts = data["Facts"]
            query = data["Query"]
            proof = data["Proof"]
            semantics = declaration + '; ' + facts + '; ' + query + '; ' + proof
            sim_shots, question_concepts, question_operators = find_shots(semantics, train_datas)
            final_shot_prompt = 'Some Examples:' + '\n'.join(sim_shots)

            semantics = data['Declarations'] + '; ' + data['Facts'] + '; ' + data['Query'] + '; ' + data['Proof']
            final_concepts = set(question_concepts + extract_concepts(semantics))
            final_operators = set(question_operators + extract_operators(semantics))

            # 构造知识方程到lean的对齐规则prompt
            al_2_lean_promt = "Conversion Rules from Assertion Logic to Lean:" + build_al_2_lean_prompt(final_concepts, final_operators)

            final_input = al_2_lean_promt + '\n\n' + final_shot_prompt + '\n\n' + answer_template.format(str(j), data['Declarations'], data['Facts'], data['Query'], data['Proof'])
            
            # print(instruction + '\n\n' + final_input)

            completion = client.chat.completions.create(
                model="deepseek-v3-241226",
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": final_input},
                ],
            )
            ans = completion.choices[0].message.content
        
            print(ans)
            print('####################################################')
            print('\n\n')
            data.update({"llm_lean": ans})
            json.dump(data,f1,ensure_ascii=False,indent=4)
            f1.write(',\n')
            f1.flush()  

if __name__ == "__main__":
    main()