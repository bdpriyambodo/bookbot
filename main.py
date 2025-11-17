from stats import get_num_words, get_num_char

filepath = "books/frankenstein.txt"

def main (filepath):
    print(f"Found {get_num_words(filepath)} total words")
    print(get_num_char(filepath))

main(filepath)

