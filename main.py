import sys
import os  # 用于检查文件路径是否存在
from Text_preprocessing import preprocess
from input import read_file
from construct_vector import get_word_frequency_vector
from calculate_similarity import calculate_cosine_similarity
from calculate_repetition_rate import calculate_repetition_rate
import cProfile
import pstats


def write_output(file_path, result):
    try:
        # 提取目录路径
        directory = os.path.dirname(file_path)

        # 如果目录不存在，则创建目录
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # 尝试写入结果到文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{result}%")

    except OSError as e:
        # 捕获由于无效路径或文件名导致的错误
        print(f"Error: Could not write to file '{file_path}'. Reason: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("错误: 需要提供三个文件路径作为参数，第一个为原文件路径，第二个为抄袭文件路径，第三个为输出文件路径")
        print("例: 'D:\\software_engineering\\test\\orig.txt'")
        sys.exit(1)  # 退出程序，状态码为1表示异常退出
    # 从命令行参数获取文件路径
    orig_file = sys.argv[1]
    plag_file = sys.argv[2]
    output_file = sys.argv[3]
    # 开启性能分析
    pr = cProfile.Profile()
    pr.enable()
    # 检查文件路径是否存在
    if not os.path.exists(orig_file):
        print(f"错误: 原始文件路径 '{orig_file}' 不存在.")
        sys.exit(1)

    if not os.path.exists(plag_file):
        print(f"错误: 抄袭文件路径 '{plag_file}' 不存在.")
        sys.exit(1)
    # 测试
    # orig_file = "D:\\software_engineering\\Paper_plagiarism_check\\test\\orig.txt"
    # plag_file = "D:\software_engineering\Paper_plagiarism_check\test\orig_0.8_del.txt"

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
    # 结束性能分析
    pr.disable()
    stats = pstats.Stats(pr)
    stats.strip_dirs().sort_stats('cumulative').print_stats()  # 打印性能分析结果
    # 输出结果，将重复率写入到指定的路径中
    write_output(output_file, repetition_rate)
    print(f"重复率：{repetition_rate}")
