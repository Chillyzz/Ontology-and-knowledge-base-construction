import json

# 读取并处理 JSON 数据
def process_concepts(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        # 读取整个文件并解析为 JSON 列表
        data = json.load(infile)
        
        # 检查数据是否为列表
        if not isinstance(data, list):
            print("输入的 JSON 数据不是列表格式，请检查文件内容。")
            return
        
        # 用于保存提取和处理后的 concepts
        processed_concepts = []
        
        # 处理每个对象中的 concepts 字段
        for item in data:
            if isinstance(item, dict) and 'concepts' in item:
                concepts = item['concepts']
                
                # 将字符串中的 JSON 格式数据转换为列表
                try:
                    concepts_list = json.loads(concepts.strip('```json\n').strip())
                    
                    # 处理为逗号分隔的字符串
                    formatted_concepts = ', '.join(concepts_list)
                    
                    # 添加到结果列表
                    processed_concepts.append(formatted_concepts)
                except json.JSONDecodeError:
                    print(f"Invalid 'concepts' format in: {concepts}")
        
        # 保存提取和处理后的 concepts 到新文件
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            json.dump(processed_concepts, outfile, ensure_ascii=False, indent=4)
            
        print(f"处理后的 concepts 数据已保存到 {output_file_path}")

# 示例调用
if __name__ == "__main__":
    input_file_path = '/home/zjy17/Conic10k/test_data/probability_concept.json'  # 替换为输入文件路径
    output_file_path = '/home/zjy17/Conic10k/test_data/probability.json'  # 替换为输出文件路径
    process_concepts(input_file_path, output_file_path)

