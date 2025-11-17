from enum import unique


def get_book_text(filepath):
    # filepath = "/home/bdp/project/learning/workspace/github.com/bdpriyambodo/bookbot/books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

def get_num_words(filepath):
    text_book = get_book_text(filepath)
    total_word = len(text_book.split())
    return total_word

def get_num_char(filepath):
    text_book = get_book_text(filepath).lower()
    chars = list(text_book)
    unique_chars = sorted(set(chars))
    char_count = {}
    for c in unique_chars:
        char_count[c] = chars.count(c)
    return char_count
    # print(f"Total characters: {len(chars)}")
    # print(f"Total unique characters: {len(unique_chars)}, All: {unique_chars}")
    # print(char_count)


# TEST
# filepath = "books/frankenstein.txt"
# get_num_char(filepath)



