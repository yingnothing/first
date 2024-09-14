import sys


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)
#
# if __name__ == "__main__":
#     orig_file = sys.argv[1]
#     plag_file = sys.argv[2]
#     output_file = sys.argv[3]
#
#     original_text = read_file(orig_file)
#     plagiarized_text = read_file(plag_file)