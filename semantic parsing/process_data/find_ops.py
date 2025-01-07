import re
import json

def extract_ops(text, declarations, facts, querys):
    pattern = r'\b(\w+)\('  # 匹配以括号开始的部分
    ops = []

    declarations = declarations.split('; ')
    facts = facts.split('; ')
    querys = querys.split('; ')

    for fact in facts:
        op_matches = re.findall(pattern, fact)
        ops.extend(op_matches)
    
    for query in querys:
        op_matches = re.findall(pattern, fact)
        ops.extend(op_matches)

    return list(set(ops))
    
    
def find_ops_in_text(text):
    final_ops = []
    text_ops = open('/home/zcl/conic10k/Refine/text_to_ops.json','r',encoding='utf-8')
    text_to_ops = json.load(text_ops)

    for key in text_to_ops.keys():
        if key in text:
            final_ops.extend(text_to_ops[key])
    return list(set(final_ops))