from stats import get_num_words, get_num_char
import sys

# filepath = "books/frankenstein.txt"

def main (filepath):
    # print(f"Found {get_num_words(filepath)} total words")
    # print(get_num_char(filepath))
    char_count_list = get_num_char(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}..")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")

    # print((char_count_list))
    for c in char_count_list:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['count']}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    main(filepath)

