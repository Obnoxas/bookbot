def count_words(book_text):
    word_count = len(str.split(book_text))
    return print(f"{word_count} words found in the document")

def count_characters(book_text):
    lowered_text = str.lower(book_text)
    letter_count = {}
    for letter in lowered_text:
        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1
    return print(letter_count)