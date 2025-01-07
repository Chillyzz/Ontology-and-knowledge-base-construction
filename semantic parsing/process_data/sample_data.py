import json
import random

def extract_data(indices):
    with open('/data/zcl/conic10k/eval_models/outputs/extrac_answer/baseline/deepseek-math-7b-rl-by-gpt4o.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)
    result = []
    for index in indices:
        result.append(datas[index])
    with open('/data/zcl/conic10k/eval_models/outputs/extrac_answer/baseline/deepseek-math-7b-rl-by-gpt4o_300.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/deepseek-math-7b-rl-baseline.json', 'r', encoding='utf-8') as f:
    #     datas = json.load(f)
    # result = []
    # for index in indices:
    #     result.append(datas[index])
    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/deepseek-math-7b-rl-baseline_300.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)


    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/deepseek-math-7b-rl-with-assertion.json', 'r', encoding='utf-8') as f:
    #     datas = json.load(f)
    # result = []
    # for index in indices:
    #     result.append(datas[index])
    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/deepseek-math-7b-rl-with-assertion_300.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)

    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/llama-3-8b-baseline.json', 'r', encoding='utf-8') as f:
    #     datas = json.load(f)
    # result = []
    # for index in indices:
    #     result.append(datas[index])
    # with open('/data/zcl/conic10k/eval_models/outputs/fixed_5_shot/llama-3-8b-baseline_300.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)


def extract_random_data(input_file, output_file, k, seed=None):
    # 设置随机种子，确保结果可重现
    if seed is not None:
        random.seed(seed)

    # 读取输入文件中的JSON数据
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 获取数据长度
    data_length = len(data)

    # 确保k不超过数据总数
    k = min(k, data_length)

    # 随机抽取k条数据的索引
    indices = random.sample(range(data_length), k)

    # 通过索引获取对应的数据
    random_data = [data[i] for i in indices]
    
    # 将随机抽取的数据保存到输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(random_data, f, ensure_ascii=False, indent=4)
    
    # 返回抽取的数据的索引
    return indices

# # 示例用法
# input_file = '/data/zcl/conic10k/conic10k/test.json'  # 输入的JSON文件名
# output_file = '/data/zcl/conic10k/eval_models/test_300.json'  # 输出的JSON文件名
# k = 300  # 要抽取的数据条数
# seed = 42  # 固定的随机种子

# indices = extract_random_data(input_file, output_file, k, seed)
# print("Indices of extracted data:", indices)
indices = [57, 12, 140, 125, 114, 71, 52, 279, 44, 216, 16, 15, 47, 111, 119, 258, 13, 101, 292, 214, 112, 229, 142, 3, 81, 290, 174, 277, 79, 110, 172, 293, 287, 194, 49, 183, 176, 135, 22, 235, 63, 193, 40, 150, 185, 147, 265, 180, 17, 11, 169, 58, 197, 74, 20, 218, 59, 221, 25, 97, 294, 116, 162, 213, 93, 41, 94, 90, 53, 171, 68, 179, 273, 165, 18, 155, 237, 43, 136, 186, 62, 234, 118, 240, 69, 163, 263, 272, 56, 175, 83, 196, 198, 14, 248, 8, 80, 102, 278, 289, 54, 145, 264, 203, 199, 167, 127, 282, 164, 117, 36, 67, 35, 259, 143, 137, 188, 149, 109, 182, 202, 92, 211, 187, 130, 126, 23, 298, 28, 39, 160, 257, 108, 152, 200, 98, 274, 166, 285, 262, 64, 141, 2, 29, 184, 201, 87, 230, 75, 286, 168, 238, 0, 247, 128, 45, 129, 27, 76, 255, 50, 170, 95, 244, 249, 254, 82, 296, 4, 223, 178, 78, 61, 7, 30, 281, 72, 121, 10, 122, 260, 219, 104, 204, 280, 154, 191, 226, 124, 84, 60, 70, 21, 33, 146, 77, 195, 212, 215, 96, 161, 88, 241, 91, 138, 51, 85, 209, 267, 177, 66, 299, 288, 31, 210, 148, 222, 157, 151, 266, 156, 275, 99, 134, 9, 227, 271, 270, 131, 42, 207, 65, 132, 236, 217, 228, 256, 46, 243, 232, 189, 284, 105, 153, 139, 113, 233, 26, 269, 6, 55, 208, 159, 261, 100, 268, 73, 276, 242, 253, 48, 115, 107, 252, 181, 231, 34, 190, 123, 283, 5, 86, 206, 246, 133, 144, 251, 224, 1, 245, 173, 158, 38, 291, 297, 205, 220, 103, 295, 24, 225, 19, 120, 192, 250, 32, 89, 37, 239, 106]
extract_data(indices)

