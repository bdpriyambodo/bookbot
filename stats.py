def get_book_text(filepath):
    # filepath = "/home/bdp/project/learning/workspace/github.com/bdpriyambodo/bookbot/books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

def get_num_words(filepath):
    text_book = get_book_text(filepath)
    total_word = len(text_book.split())
    return total_word

