import sys

from stats import get_num_words
from stats import count_characters
from stats import make_formatted_list

def get_book_text(path_to_file:str) -> str:

    with open(path_to_file) as f:
        contents = f.read()
    
    return contents


def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    num_words = get_num_words(contents)
    char_count_dict = count_characters(contents)
    formatted_list = make_formatted_list(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in formatted_list:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")
    pass

main()
