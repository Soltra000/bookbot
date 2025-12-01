import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_char_count
from stats import get_sort_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(get_num_words(filepath))
    print("--------- Character Count -------")
    for item in get_sort_dict(get_char_count(filepath)):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

