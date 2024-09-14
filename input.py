import sys


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    orig_file = sys.argv[1]
    plag_file = sys.argv[2]
    output_file = sys.argv[3]

    original_text = read_file(orig_file)
    plagiarized_text = read_file(plag_file)