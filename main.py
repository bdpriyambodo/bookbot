from stats import get_num_words

filepath = "books/frankenstein.txt"

def main (filepath):
    print(f"Found {get_num_words(filepath)} total words")

main(filepath)

