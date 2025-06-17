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
    return letter_count

def sort_key(dict):
    return dict["num"]

def sort_dictionaries(letter_count):
    sorted_dictionaries = []
    for character in letter_count:
        sorter = {}
        sorter["char"] = character
        sorter["num"] = letter_count[character]
        sorted_dictionaries.append(sorter)
    sorted_dictionaries.sort(reverse=True, key=sort_key)
    return print(sorted_dictionaries)