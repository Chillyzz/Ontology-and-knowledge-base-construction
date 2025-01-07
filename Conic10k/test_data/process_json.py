import json

# 读取并修正 JSON 文件格式
def fix_json_format(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
        
        # 修正格式：为多个对象之间添加逗号，并包裹在一个数组中
        fixed_content = f"[{content.replace('}{', '},{')}]"
        
        try:
            # 将修正后的内容解析为有效的 JSON 格式
            data = json.loads(fixed_content)
            
            # 将修正后的数据保存到新的文件
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
                
            print(f"修正后的数据已保存到 {output_file_path}")
        except json.JSONDecodeError:
            print("修正后的 JSON 格式无效，请检查输入文件的内容。")

# 示例调用
if __name__ == "__main__":
    input_file_path = '/home/zjy17/Conic10k/test_data/concept_extract.json'  # 替换为输入文件路径
    output_file_path = '/home/zjy17/Conic10k/test_data/concept_new.json'  # 替换为输出文件路径
    fix_json_format(input_file_path, output_file_path)
