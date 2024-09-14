import math


def calculate_cosine_similarity(vector1, vector2):
    # 计算余弦相似度
    dot_product = sum(vector1[word] * vector2.get(word, 0) for word in vector1)
    magnitude1 = math.sqrt(sum([count ** 2 for count in vector1.values()]))
    magnitude2 = math.sqrt(sum([count ** 2 for count in vector2.values()]))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)
