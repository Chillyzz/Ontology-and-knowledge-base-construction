import random
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

# def embedding(datas):
#     model = SentenceTransformer('/data/pretrain_model/m3e-base-10-10-13')
#     text = []
#     for data in datas:
#         text.append(data['text'])
#     embeddings = model.encode(text)
#     # 保存嵌入向量到 .npy 文件
#     np.save('/data/zcl/conic10k/data_generate/test_embeddings.npy', embeddings)


# def k_cluster_cos(datas):
#     # 读取嵌入向量
#     loaded_embeddings = np.load('/data/zcl/conic10k/data_generate/test_embeddings.npy')
#     # 使用 K-Means 进行聚类
#     num_clusters = 20
#     kmeans = KMeans(n_clusters=num_clusters, random_state=0)
#     kmeans.fit(loaded_embeddings)

#     # 获取每个样本的聚类标签
#     labels = kmeans.labels_

#     # 获取每个簇的中心
#     cluster_centers = kmeans.cluster_centers_

#     # 找到每个簇中心对应的原始文本
#     for i in range(num_clusters):
#         cluster_center = cluster_centers[i].reshape(1, -1)  # 确保形状正确
#         # 计算每个样本与簇中心的余弦相似度
#         similarities = cosine_similarity(loaded_embeddings, cluster_center)
#         # 找到相似度最高的样本
#         closest_index = np.argmax(similarities)
#         closest_text = datas[closest_index]
#         text = closest_text['text']
#         declarations = closest_text['declarations'].strip().replace(';','\n')
#         facts = closest_text['facts'].strip().replace(';','\n')
#         query = closest_text['query']
#         print(f"现在，请你翻译下面这个数学题：\n{text}\n\n翻译结果：\n```\nDeclarations:\n{declarations}\n\nFacts:\n{facts}\n\nQuery:\n{query}\n```\n\n")

    

# def k_cluster(datas):
#     # 读取嵌入向量
#     loaded_embeddings = np.load('/data/zcl/conic10k/data_generate/train_answer_embeddings.npy')
#     # 使用 K-Means 进行聚类
#     num_clusters = 5
#     kmeans = KMeans(n_clusters=num_clusters, random_state=0)
#     kmeans.fit(loaded_embeddings)

#     # 获取每个样本的聚类标签
#     labels = kmeans.labels_

#     # 获取每个簇的中心
#     cluster_centers = kmeans.cluster_centers_

#     # 找到每个簇中心对应的原始文本
#     for i in range(num_clusters):
#         cluster_center = cluster_centers[i].reshape(1, -1)  # 确保形状正确
#         # 计算每个样本与簇中心的余弦相似度
#         similarities = cosine_similarity(loaded_embeddings, cluster_center)
#         # 找到相似度最高的样本
#         closest_index = np.argmax(similarities)
#         closest_text = datas[closest_index]
#         text = closest_text['text']
#         print(f"请你解答以下的数学问题，不用给出解答过程，直接给出该问题的答案。\n问题：{text}\n答案：{closest_text['answer_expressions']}\n\n")
#         # declarations = closest_text['declarations'].strip().replace(';','\n')
#         # facts = closest_text['facts'].strip().replace(';','\n')
#         # query = closest_text['query']
#         # print(f"现在，请你翻译下面这个数学题：\n{text}\n\n翻译结果：\n```\nDeclarations:\n{declarations}\n\nFacts:\n{facts}\n\nQuery:\n{query}\n```\n\n")


def main():
    train_f = r'/home/zcl/conic10k/conic10k/train.json'
    train = open(train_f,'r',encoding='utf-8')
    train_datas = json.load(train)
    embedding(train_datas)
    k_cluster_cos(train_datas)


main()
