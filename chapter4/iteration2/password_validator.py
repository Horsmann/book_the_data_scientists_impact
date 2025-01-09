import re

def is_valid(password: str) -> bool:

    match_length = len(password) >= 8
    match_lowercase_alpha = bool(re.search("[a-z]+", password))
    match_uppercase_alpha = bool(re.search("[A-Z]+", password))
    match_number_alpha = bool(re.search("[0-9]+", password))
    match_symbol = bool(re.search("[^\\w\\d]+", password))

    match_year = not bool(re.findall("(?:19|20)\\d{2}", password))

    return (match_year and 
            match_length and 
            match_lowercase_alpha and 
            match_uppercase_alpha and 
            match_number_alpha and match_symbol)
