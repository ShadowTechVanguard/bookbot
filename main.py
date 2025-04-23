import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    from stats import get_num_words, char_frequency, read_book, sorted_char_list
    txt = sys.argv[1]
    read = read_book(txt)
    char = char_frequency(read)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {txt}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(read)} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list(char):
        print(f"{item['Char']}: {item['Num']}")
        if item == len(sorted_char_list(char)):
            break
    print("============= END ===============")

main()