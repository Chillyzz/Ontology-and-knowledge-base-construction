import difflib
import json
import heapq
import math
import Levenshtein
import random
import numpy as np
import re
# from sentence_transformers import SentenceTransformer

# # 余弦相似度
# def cosimilarity(text,datas):
#     model = SentenceTransformer('/data/pretrain_model/m3e-base-10-10-13')
#     text_vec = model.encode(text)
#     embeddings = model.encode(datas)
#     sims = []
#     for sentence, embedding in zip(datas, embeddings):
#         dot_product = np.dot(text_vec, embedding)
#         norm_vec1 = np.linalg.norm(text_vec)
#         norm_vec2 = np.linalg.norm(embedding)
#         sims.append(dot_product / (norm_vec1 * norm_vec2))
#     return sims


# # 编辑距离
# def EditDistance(text,datas):
#     sims = []
#     for data in datas:
#         sims.append(Levenshtein.distance(text,data))
#     return sims


# Jaro 距离
def JaroDistance(text,datas):
    sims = []
    for data in datas:
        r = Levenshtein.jaro(text,data)
        sims.append(r)
    return sims


# # J-W 距离
# def JWDistance(text,train_datas,k):
#     sims = []
#     for data in datas:
#         r = Levenshtein.jaro_winkler(text,data)
#         sims.append(r)
#     return sims

# 所有字符串匹配比例
def match_ratio(text,datas):
    similaritys = []
    for data in datas:
        similaritys.append(difflib.SequenceMatcher(None,text,data).quick_ratio())
    return similaritys

# def random_shot(train_datas,k):
#     random_data = random.sample(train_datas, k)
#     return random_data

pattern = r"\$.*?\$"

def find_top_k(text,train_datas,k):
    datas = []
    for data in train_datas:
        datas.append(re.sub(pattern, "A", data['text']))
        # datas.append(data['text'])
    # res = match_ratio(re.sub(pattern, "", text), datas)
    res_1 = JaroDistance(re.sub(pattern, "A", text), datas)
    res_2 = match_ratio(re.sub(pattern, "A", text), datas)
    largest_k_1 = heapq.nlargest(k,res_1)
    largest_k_2 = heapq.nlargest(k,res_2)

    result = []
    for index,value in enumerate(res_1):
        if value in largest_k_1:
            result.append(train_datas[index])
    for index,value in enumerate(res_2):
        if value in largest_k_2:
            result.append(train_datas[index])

    final_result = []
    ids = []
    for res in result:
        ids.append(res['id'])
    final_ids = set(ids)
    for index in final_ids:
        i = ids.index(index)
        final_result.append(result[i])
    return final_result

    