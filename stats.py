def get_num_words(book_text):
    words = book_text.split()
    count = len(words)
    return (count)

def get_distinct_char(book_text):
    words = book_text.split()
    char_list = []
    for word in words:
        char = word.split()
        for ch in char:
            ch = ch.lower()
        for c in ch:
            char_list.append(c)
    distinct_count = dict(zip(set(char_list), [char_list.count(x) for x in set(char_list)]))
    return distinct_count