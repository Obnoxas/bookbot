def main():

    from stats import count_words, count_characters, sort_dictionaries

    def get_book_text():
        book_text = f.read()
        return book_text
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    with open("books/frankenstein.txt") as f:
        count_words(get_book_text())
    
    print("--------- Character Count -------")

    with open("books/frankenstein.txt") as f:
        count_characters(get_book_text())

    with open("books/frankenstein.txt") as f:
        sorted_dictionaries = sort_dictionaries(count_characters(get_book_text()))

    for character in sorted_dictionaries:
        if str.isalpha(character["char"]) is True:
            print(f"{character["char"]}: {character["num"]}")

main()