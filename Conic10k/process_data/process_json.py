# 将翻译好的text按句子划分成new_text

import json

def split_sentences(data):
    """
    将数据中的 `new_text` 字段按换行符 `\n` 分割成句子列表。
    """
    if 'new_text' in data and isinstance(data['new_text'], str):
        # 按照换行符分割，并去掉空白字符，确保句子以 '.' 结尾
        sentences = [sentence.strip() + "." if not sentence.strip().endswith('.') else sentence.strip()
                     for sentence in data['new_text'].split("\n") if sentence.strip()]
        data['new_text'] = sentences
    return data

def process_json(input_file, output_file):
    """
    处理 JSON 文件，将 `new_text` 按换行符分割成句子列表，并保存到新文件中。
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # 逐条处理数据
    processed_data = [split_sentences(entry) for entry in json_data]

    # 将处理后的数据写入新的文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)

def main():
    input_file = r"/home/zjy17/Conic10k/conic10k/translation_test.json"  # 替换为你的输入文件路径
    output_file = r"/home/zjy17/Conic10k/conic10k/translation_new.json"  # 替换为你的输出文件路径

    process_json(input_file, output_file)
    print(f"处理完成！处理后的数据已保存到 {output_file}")

if __name__ == '__main__':
    main()
