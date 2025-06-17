def main():

    import sys

    from stats import count_words, count_characters, sort_dictionaries

    def get_book_text():
        book_text = f.read()
        return book_text
    
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")

        with open(sys.argv[1]) as f:
            count_words(get_book_text())
        
        print("--------- Character Count -------")

        with open(sys.argv[1]) as f:
            count_characters(get_book_text())

        with open(sys.argv[1]) as f:
            sorted_dictionaries = sort_dictionaries(count_characters(get_book_text()))

        for character in sorted_dictionaries:
            if str.isalpha(character["char"]) is True:
                print(f"{character["char"]}: {character["num"]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()