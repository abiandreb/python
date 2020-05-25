import re


def no_invalid_char(word):
    regex = re.compile('[@!#$%^&*()<>?/|}{~:]')
    if regex.search(word) is None:
        return False
    else:
        return True


def valid_password(word):
    if any(char.isdigit() for char in word) and any(char.isalpha() for char in word):
        return True




