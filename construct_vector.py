# 计算每个字出现的次数
from collections import Counter


def get_word_frequency_vector(words):
    word_freq = Counter(words)
    return word_freq
