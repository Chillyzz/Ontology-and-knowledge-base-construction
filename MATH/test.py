# 把文件夹下的json文件中的问题写到一个json里面

import os
import json

# 定义文件夹路径
input_folder = "/home/zjy17/MATH/test/algebra"  # 替换为包含 JSON 文件的文件夹路径
output_file = "/home/zjy17/MATH/test.json"

# 初始化结果列表
problems = []

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):  # 只处理 JSON 文件
        file_path = os.path.join(input_folder, filename)
        try:
            # 打开并读取 JSON 文件
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # 提取 "problem" 值并存储为独立的字典项
                if "problem" in data:
                    problems.append({"problem": data["problem"]})
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# 将所有问题写入新的 JSON 文件
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=4, ensure_ascii=False)

print(f"提取完成！结果已保存到 {output_file}")
