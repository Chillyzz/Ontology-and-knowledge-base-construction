import json
from openai import OpenAI

# Deepseek API 配置
API_KEY = "sk-8532a64c13f74a4392e94db560073553"  # 替换为您的 Deepseek API 密钥
BASE_URL = "https://api.deepseek.com"

# Deepseek API 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 指令：提取数学概念
instruction = (
    "You are a professional mathematics assistant. Given a math problem, "
    "identify the top 3 most important mathematical concepts involved in solving the problem. "
    "Return the concepts as a JSON list of strings, with each concept described concisely in English."
)

# 输入文件路径
input_file = "/home/zjy17/MATH/prealgebra.json"  # 替换为您的 JSON 文件路径
output_file = "/home/zjy17/Conic10k/test_data/prealgebra_extract.json"

# 读取测试数据
with open(input_file, "r", encoding="utf-8") as f:
    problems_data = json.load(f)

# 输出结果列表
results = []

# 遍历每个问题，调用 Deepseek API 提取概念
for idx, item in enumerate(problems_data):
    problem_text = item.get("problem", "").strip()
    if not problem_text:
        print(f"问题 {idx} 无内容，跳过")
        continue

    print(f"处理问题 {idx}: {problem_text}")

    # 构造输入数据
    response = client.chat.completions.create(
        model="deepseek-coder",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": problem_text},
        ],
        stream=False
    )

    # 获取 Deepseek 的回答
    extracted_concepts = response.choices[0].message.content.strip()
    print(f"问题 {idx} 的概念提取结果: {extracted_concepts}")

    # 保存结果
    result = {
        "problem": problem_text,
        "concepts": extracted_concepts  # 解析 Deepseek 返回的 JSON 格式概念
    }
    results.append(result)

    # 每次提取完一个问题后立即将结果保存到输出文件
    with open(output_file, "a", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"问题 {idx} 的概念已保存")
    
print(f"提取完成！结果已保存到 {output_file}")

