def count_characters(text):
    """Count all the characters in a text

    Args:
        text (str): the text to counted

    Returns:
        dict: dictionary of characters and their count(value)
    """
    char_dict = {}
    text = text.lower()
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
            continue
        char_dict[char] += 1
    return char_dict

def count_words(text):
    """Count all words in the text

    Args:
        text (str): the text to be counted

    Returns:
        int: total number of words
    """
    return len(text.split())

def print_book_report(book):
    """Create a report about the book

    Args:
        book (str): the book

    Returns:
        str: the report
    """
    header = "--- Begin report of books/frankenstein.txt ---\n"
    word_count = f"{count_words(book)} words found in the document\n"
    footer = "--- End report ---"
    report = ""
    character_count = count_characters(book)
    for char in character_count:
        if char.isalpha():
            report += f"The '{char}' character was found {character_count[char]} times\n"
    return header + word_count + report + footer



with open('./books/frankenstein.txt', 'r') as f:
    book_contents = f.read()
    print(print_book_report(book_contents))

