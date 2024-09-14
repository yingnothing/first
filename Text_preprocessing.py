# 将文本进行处理
import jieba
import re


def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text)  # 去除标点符号
    words = list(jieba.cut(text))  # 使用 jieba 进行中文分词
    return words
