import transformers
import torch
import json
import re
import sys
sys.path.append('/home/zjy17/Conic10k')

from process_data.compute_similarity import find_top_k
from openai import OpenAI

instruction =  """
You are a professional extractor. When you are given a LaTeX-like formatted text about a math problem, extract useful information from the following information:
1. Theorems (Theorem)
2. Definitions (Definition)
3. Equations (Equation)
4. Corollarys (Corollary)

Return the extracted information in this format:
{
    "Theorem": "<Title of the Theorem or Statement of the Theorem>",
    "id": "<Unique Identifier or Theorem Number>",
    "Equation": "<Mathematical Formula in LaTeX>",
    "Content": "<Detailed Explanation or Application of the Theorem>"
}

Make sure to include equations within $$ signs.

Here are some examples:

\section*{Theorem 2.4.4}
The product of GCD and LCM of two numbers is equal to the product of the two numbers:

$$
G C D(m, n) \cdot \operatorname{LCM}(m, n)=m \cdot n
$$

\section*{Theorem 2.4.5}
If two numbers have a common factor $c$, then

$$
\operatorname{gcd}(a c, b c)=c \cdot \operatorname{gcd}(a, b)
$$

You should return a json file like this:
[
    {
        "Theorem": "The product of GCD and LCM of two numbers is equal to the product of the two numbers.",
        "id": "2.4.4",
        "Equation": "$$ GCD(m, n) \\cdot \\operatorname{LCM}(m, n) = m \\cdot n $$",
        "Content": "This theorem states that for any two integers m and n, the product of their greatest common divisor (GCD) and least common multiple (LCM) is equal to the product of the two numbers themselves. This relationship helps in simplifying calculations in number theory, especially when working with divisibility and multiples."
    },
    {
        "Theorem": "If two numbers have a common factor c, then gcd(a c, b c) = c ⋅ gcd(a, b).",
        "id": "2.4.5",
        "Equation": "$$ \\operatorname{gcd}(a c, b c) = c \\cdot \\operatorname{gcd}(a, b) $$",
        "Content": "This theorem describes the behavior of the GCD function when two numbers share a common factor c. It asserts that the greatest common divisor of ac and bc is the product of c and the GCD of a and b. This property is useful when working with scaled versions of numbers and helps simplify calculations in factorization and divisibility."
    }
]

"""

output_file = "/home/zjy17/Conic10k/Few_shot/extracted_definition.json"

def main():
    client = OpenAI(api_key='sk-56a4ejBaNLcRbTiZfnbIX6L6i3lDzuCdscWRhPO1TR5tQfnJ', base_url='https://api.chatanywhere.tech/v1')

    # 读取 AMC.txt 文件的内容
    with open('/home/zjy17/PDF_OCR/AMC_Ch1.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()

    # 构造模型输入
    final_input = f"{instruction}\n\nInput Text:\n{input_text}"

    response = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": final_input},
    ],
    stream=False
    )

    # 获取模型的输出结果
    result = response.choices[0].message.content

    # 打印和保存结果
    print(f"Extracted Content:\n{result}")
    print(result)
    
    # 将 result 转换为字符串，并直接写入文件
    with open("extracted_theorem_Ch1.txt", "w", encoding="utf-8") as f_out:
        f_out.write(result)
    
    
if __name__ == "__main__":
    main()