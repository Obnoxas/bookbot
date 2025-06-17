def main():

    from stats import count_words, count_characters, sort_dictionaries

    def get_book_text():
        book_text = f.read()
        return book_text
    
    with open("books/frankenstein.txt") as f:
        count_words(get_book_text())
        
    with open("books/frankenstein.txt") as f:
        count_characters(get_book_text())

    with open("books/frankenstein.txt") as f:
        sort_dictionaries(count_characters(get_book_text()))


main()