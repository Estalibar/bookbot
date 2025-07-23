from stats import get_num_words, get_distinct_char, pretty_list
import sys

#Usage: python3 main.py <path_to_book>

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text()
    num_words = get_num_words(book_text)
    num_char = get_distinct_char(book_text)
    sorted_list = pretty_list(num_char)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in sorted_list:
        key, value = list(char_count.items())[0]
        print(f"{key}: {value}")
    print("============= END ===============")

main()