import sys
from Text_preprocessing import preprocess
from input import read_file
from construct_vector import get_word_frequency_vector
from calculate_similarity import calculate_cosine_similarity
from calculate_repetition_rate import calculate_repetition_rate
if __name__ == "__main__":
    # 从命令行参数获取文件路径
    orig_file = sys.argv[1]
    plag_file = sys.argv[2]
    # orig_file = "D:\\software_engineering\\test\\orig.txt"
    # plag_file = "D:\\software_engineering\\test\\orig_0.8_add.txt"
    # 读取文本并进行预处理
    original_text = preprocess(read_file(orig_file))
    plagiarized_text = preprocess(read_file(plag_file))

    # 生成词频向量
    original_vector = get_word_frequency_vector(original_text)
    plagiarized_vector = get_word_frequency_vector(plagiarized_text)

    # 计算余弦相似度
    cosine_similarity = calculate_cosine_similarity(original_vector, plagiarized_vector)

    # 计算重复率
    repetition_rate = calculate_repetition_rate(cosine_similarity)

    # 输出结果
    print(repetition_rate)