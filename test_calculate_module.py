import unittest
from Text_preprocessing import preprocess
from construct_vector import get_word_frequency_vector
from calculate_similarity import calculate_cosine_similarity
from calculate_repetition_rate import calculate_repetition_rate


class TestPlagiarismCheck(unittest.TestCase):
    def test_preprocess(self):
        text = "这是一个测试文本，用来测试预处理功能。"
        expected_output = ['这是', '一个', '测试', '文本', '用来', '测试', '预处理', '功能']
        self.assertEqual(preprocess(text), expected_output)

    def test_get_word_frequency_vector(self):
        words = ['测试', '测试', '文本']
        expected_output = {'测试': 2, '文本': 1}
        self.assertEqual(get_word_frequency_vector(words), expected_output)

    def test_calculate_cosine_similarity(self):
        vector1 = {'测试': 2, '文本': 1}
        vector2 = {'测试': 1, '文本': 1}
        similarity = calculate_cosine_similarity(vector1, vector2)
        self.assertAlmostEqual(similarity, 0.9487, places=4)

    def test_calculate_cosine_similarity_with_zero_vector(self):
        vector1 = {'测试': 0}
        vector2 = {'文本': 0}
        similarity = calculate_cosine_similarity(vector1, vector2)
        self.assertEqual(similarity, 0.0)

    def test_calculate_repetition_rate(self):
        cosine_similarity = 0.9
        repetition_rate = calculate_repetition_rate(cosine_similarity)
        self.assertEqual(repetition_rate, 90.0)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
