import transformers
import torch
import json
import re
import sys
sys.path.append('/home/zcl/conic10k')

from process_data.compute_similarity import find_top_k
from openai import OpenAI

instruction = "You are a professional translator. When you are given a Chinese text about a math problem, you need to break it down into multiple simple sentences and make sure that each simple sentence is a complete statement, that is, each entity variable has its own name. And add $ signs on both sides of the variables and formulas."

shots_template = '''
Example {}:
Chinese Text:
{}

Translation Result:
{}
'''

answer_template = '''
Chinese Text:
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

    test_f = r'/home/zcl/conic10k/conic10k/top_300_test.json'
    output = r'/home/zcl/conic10k/conic10k/top_300_test_with_new_text.json'

    shots_file = open('/home/zcl/conic10k/conic10k/top_200_rich_datas_cluster_with_text_2_ops.json','r',encoding='utf-8')
    shots_data = json.load(shots_file)

    test = open(test_f,'r',encoding='utf-8')
    f1 = open(output,'a',encoding='utf-8')

    test_datas = json.load(test)
    answers = []
    
    for j, data in enumerate(test_datas):
        # if 0 <= j < 100:
            d = dict()
            question = data['text']
            print(f"问题：\n{question}")

            # 寻找前3个shot
            few_shots = []
            sim_res = find_top_k(question,shots_data,3)
            for i,res in enumerate(sim_res):
                text = res['text']
                new_text = res['new_text']
                few_shots.append(shots_template.format(str(i+1), text, '\n'.join(new_text)))
            final_shots = '\n'.join(few_shots)


            final_input = final_shots + '\n\n' + answer_template.format(question)

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
            d['text'] = question
            ans = response.choices[0].message.content
            d['new_text'] = ans
            d['fact_expressions'] = data['fact_expressions']
            d['query_expressions'] = data['query_expressions']

            print(f"\n\n回答：\n{ans}\n\n")

            json.dump(d,f1,ensure_ascii=False,indent=4)
            f1.write(',\n')
            f1.flush()
        

if __name__ == "__main__":
    main()