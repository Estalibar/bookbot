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

def pretty_list(char_dict):
    pretty_list = []
    for char in char_dict:
        pretty_list.append({char: char_dict[char]}) if char.isalpha() and char in char_dict else None
    pretty_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    return pretty_list