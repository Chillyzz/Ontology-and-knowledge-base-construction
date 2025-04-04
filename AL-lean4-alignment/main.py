import json
import re

# 概念转换规则
type_rules = {
    "Function": "ℝ -> ℝ",
    "Polynomial": "Polynomial ℝ",
    "Set": "Set ℝ",
    "NonNegativeNumbers": "NNReal",
    "Integers": "ℤ",
    "Integer": "ℤ",
    "Real": "ℝ",
    "RationalNumbers": "ℚ",
    "ComplexNumbers": "ℂ",
    "Sequence": "ℕ -> ℝ",
    "PositiveIntegers": "ℕ",
    "NaturalNumbers": "ℕ",
    "PositiveInteger": "ℕ"
}

# 定义所有使用 subtype 约束的类型
subtype_types = {
    "NegativeNumbers",
    "PositiveNumbers",
    "AlgebraicNumbers",
    "IrrationalNumbers",
    "TranscendentalNumbers",
    "OddNumbers",
    "EvenNumbers",
    "NonNegativeIntegers",
    "NegativeIntegers",
    "PrimeNumbers",
    "CompositeNumbers",
    "ImaginaryNumbers"
}

def replace_vars(expression, var_map):
    """ 替换表达式中的变量 """
    """ 替换表达式中的变量 """
    if not expression or not var_map:  # 处理空值
        return expression
    pattern = r'\b(' + '|'.join(map(re.escape, var_map.keys())) + r')\b'
    return re.sub(pattern, lambda m: var_map[m.group(0)], expression)


# 替换 Sqrt、Get_Number_Floor、Get_Number_Ceil、Get_Number_Round 和 Abs 函数中的括号并加上空格
def replace_function_with_space(query):
    # 替换 Sqrt、Get_Number_Floor、Get_Number_Ceil、Get_Number_Round、Abs
    query = re.sub(r"(Sqrt|Get_Number_Floor|Get_Number_Ceil|Get_Number_Round|Abs)\(", r"\1 (", query)
    return query


# 替换 多个参数的算子
def replace_function_syntax(expression):
    """
    将 Log(a, b) 转换为 Log a b
    """
    rules = {
        "Log": {
            "pattern": r"Log\s*\(\s*([^,]+)\s*,\s*([^)]+)\s*\)",
            "replacement": r"Log (\1) (\2)"
        },
        "Build_Set": {
            "pattern": r"Build_Set\s*\(\s*(?P<var>[^,]+)\s*,\s*(?P<expr>[^)]+)\s*\)",
            "replacement": r"Build_Set (λ \g<var> => \g<expr>)"
        },
        "Solve_equation": {
            "pattern": r"Solve_equation\s*\(\s*(?P<var>[^,]+)\s*,\s*(?P<expr>[^)]+)\s*\)",
            "replacement": r"Solve_equation (λ \g<var> => \g<expr>)"
        },
        "Solve_inequation": {
            "pattern": r"Solve_inequation\s*\(\s*(?P<var>[^,]+)\s*,\s*(?P<expr>[^)]+)\s*\)",
            "replacement": r"Solve_inequation (λ \g<var> => \g<expr>)"
        }
    }
    
    for rule in rules.values():
        expression = re.sub(rule["pattern"], rule["replacement"], expression)
    
    return expression

def convert_to_lean(declarations, facts, query, test_id):
    # 解析声明部分
    if declarations:
        declarations_parts = [decl.strip() for decl in declarations.split(";")]
        variables = [decl.split(":")[0].strip() for decl in declarations_parts]
        raw_types = [decl.split(":")[1].strip() for decl in declarations_parts]

        # 根据 type_rules 替换类型
        types = [type_rules.get(t, t) for t in raw_types]  # 如果 t 在规则里，就替换；否则保持原样
    else:
        variables = []
        types = []

    # **变量映射**
    var_map = {var: var for var in variables}  # 默认变量映射到自身
    for var, typ in zip(variables, types):
        if typ in subtype_types:  # **如果变量类型是 subtype**
            var_map[var] = f"{var}.val"  # **替换为 var.val**
    # 处理Facts部分
    if facts:
        facts_parts = facts.split(";")
        facts_list = [fact.strip() for fact in facts_parts]
        # **替换 Facts 里的变量**
        facts_list = [replace_vars(fact, var_map) for fact in facts_list]
        # **替换 Sqrt 函数中的括号**
        facts_list = [replace_function_syntax(fact) for fact in facts_list]
        # **替换 Sqrt 函数中的括号**
        facts_list = [replace_function_with_space(fact) for fact in facts_list]
    else:
        facts_list = []
    
    # 构建 Lean 代码
    lean_code = f"theorem test_{test_id} "  # 根据ID动态生成 theorem 名称

    # 如果有Declarations，加入变量定义
    # 逐个声明变量
    for var, typ in zip(variables, types):
        lean_code += f"({var} : {typ}) "
    
    # 添加假设部分
    for i, fact in enumerate(facts_list):
        lean_code += f"(h{i+1} : {fact}) "
    
    # 处理查询部分
    query = replace_vars(query, var_map)
    query = replace_function_syntax(query)
    query_new = replace_function_with_space(query)
    lean_code += f": {query_new} = sorry := by sorry"
    
    return lean_code

# 处理 JSON 文件的函数
def process_json_and_write_to_md(json_file, md_file):
    # 读取JSON文件，显式指定 UTF-8 编码
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 打开文件写入 Markdown 内容
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("# Lean Code Output\n\n")

        # 逐条处理 JSON 数据集中的每个问题
        for index, entry in enumerate(data, start=1):  # 使用 enumerate 来获取每条记录的索引（从1开始）
            declarations = entry.get("Declarations", "")
            facts = entry.get("Facts", "")
            query = entry.get("Query", "")

            # 转换为Lean代码
            lean_code = convert_to_lean(declarations, facts, query, test_id=index)
            
            # 写入该问题的相关信息
            f.write(f"{lean_code}\n\n")


# **测试数据**
data = {
        "Declarations": "",
        "Facts": "",
        "Query": "Solve_equation(t: Real, 3 * 3^t + Sqrt(9 * 9^t) = 18)"
}
# 转换成Lean代码
lean_code = convert_to_lean(data["Declarations"], data["Facts"], data["Query"], 11)
print(lean_code)

# 调用函数处理数据并写入md文件
process_json_and_write_to_md('E:/ICML_2025/semantic_parsing/semantic_parsing/Data/all_pools.json', 'output.md')

