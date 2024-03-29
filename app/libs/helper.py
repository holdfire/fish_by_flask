

def is_isbn_or_key(word):
    """
        word:
     """
    # isbn： isbn13由13个0到9之间的数字组成；isbn10由10个0到9之的数字组成，含有一些‘-’
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

