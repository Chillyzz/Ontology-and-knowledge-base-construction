import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json
import re
import random

# 步骤1：提取文本并分词
def tokenize(text):
    return " ".join(jieba.lcut(text))

train_f = r'/home/zcl/conic10k/raw_data/test.json'
train = open(train_f,'r',encoding='utf-8')
data = json.load(train)


# 参数配置
n_clusters = 100  # 聚类类别数
sample_per_cluster = 3  # 每类提取的样本数

pattern = r"\$.*?\$"
# 提取文本部分
texts = [re.sub(pattern, "", item["text"]) for item in data]
print(texts)
tokenized_texts = [tokenize(text) for text in texts]

# 步骤2：向量化
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tokenized_texts)

# 步骤3：K-Means 聚类
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# 步骤4：将数据按类别分组
clustered_data = {i: [] for i in range(n_clusters)}
for idx, label in enumerate(labels):
    clustered_data[label].append(data[idx])

# 步骤5：从每类中提取指定条数数据
sampled_data = {}
for cluster_id, items in clustered_data.items():
    sampled_data[cluster_id] = random.sample(items, min(sample_per_cluster, len(items)))

output = []
for cluster_id, samples in sampled_data.items():
    for sample in samples:
        output.append({"cluster_id": cluster_id, **sample})

output_path = "/home/zcl/conic10k/conic10k/top_300_test.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)