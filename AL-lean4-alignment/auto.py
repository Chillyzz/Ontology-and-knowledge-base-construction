import subprocess
import json
import re

# 读取输入文件的内容
with open('all_tactics.in', 'r') as file:
    input_data = file.read()

# 执行命令并获取输出
result = subprocess.run(
    ['lake', 'env', '/workspace/mathematics_in_lean/repl/.lake/build/bin/repl'],
    input=input_data,  # 将文件内容传递给标准输入
    capture_output=True, text=True
)

# 打印命令输出
print("命令输出：")

# 获取命令输出
output_data = result.stdout

# 以空行作为分界线，将输出分为多个部分
output_parts = output_data.strip().split('\n\n')

# 将每部分内容存储为字符串列表
json_objects = []

for line in output_parts:
    try:
        # 解析每个 JSON 字符串
        parsed_json = json.loads(line)
        json_objects.append(parsed_json)
    except json.JSONDecodeError as e:
        print(f"解析错误: {e}")

# 将解析后的 JSON 对象写入文件
output_file = "output.json"
with open(output_file, "w", encoding="utf-8") as f:
    # 在文件的开头添加左括号
    f.write("[\n")

    # 遍历每个对象并写入文件
    for i, obj in enumerate(json_objects):
        # 将每个对象转为 JSON 字符串
        json_str = json.dumps(obj, ensure_ascii=False)

        # 如果不是最后一个对象，添加逗号
        if i < len(json_objects) - 1:
            f.write(f"  {json_str},\n")
        else:
            f.write(f"  {json_str}\n")  # 最后一个对象后不加逗号

    # 在文件的末尾添加右括号
    f.write("]\n")

print(f"数据已成功写入 {output_file}")