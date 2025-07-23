from stats import get_num_words, get_distinct_char, pretty_list
import sys

#Usage: python3 main.py <path_to_book>

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        num_char = get_distinct_char(book_text)
        sorted_list = pretty_list(num_char)
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_count in sorted_list:
            key, value = list(char_count.items())[0]
            print(f"{key}: {value}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()