def get_book_text(filepath):
    # filepath = "/home/bdp/project/learning/workspace/github.com/bdpriyambodo/bookbot/books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

# def main():
#     filepath = "books/frankenstein.txt"
#     print(get_book_text(filepath))

def main ():
    filepath = "books/frankenstein.txt"
    text_book = get_book_text(filepath)
    total_word = len(text_book.split())
    print(f"Found {total_word} total words")

main()

