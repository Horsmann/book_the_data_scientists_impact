import re

def is_valid(password: str) -> bool:
    match_length = len(password) >= 8
    match_lowercase_alpha = bool(re.search("[a-z]+", password))
    match_uppercase_alpha = bool(re.search("[A-Z]+", password))

    return (match_length and match_lowercase_alpha and match_uppercase_alpha)
