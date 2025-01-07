import json

def extract_questions(jsonl_file, output_json_file):
    """
    从 JSONL 文件中提取 question 数据并存储到新的 JSON 文件中。

    参数：
        jsonl_file (str): 输入的 JSONL 文件路径。
        output_json_file (str): 输出的 JSON 文件路径。
    """
    extracted_data = []

    # 读取 JSONL 文件
    with open(jsonl_file, "r", encoding="utf-8") as infile:
        for line in infile:
            item = json.loads(line.strip())  # 每行是一个 JSON 对象
            if "question" in item:
                extracted_data.append({"text": item["question"]})

    # 写入新的 JSON 文件
    with open(output_json_file, "w", encoding="utf-8") as outfile:
        json.dump(extracted_data, outfile, ensure_ascii=False, indent=4)

    print(f"提取完成，结果已保存到: {output_json_file}")

# 使用示例
input_file = "/home/zjy17/Conic10k/conic10k/openai.jsonl"  # 替换为你的 JSONL 文件路径
output_file = "/home/zjy17/Conic10k/conic10k/new_openai.json"  # 替换为目标 JSON 文件路径
extract_questions(input_file, output_file)
print("成功")