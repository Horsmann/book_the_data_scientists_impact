import re

def check_sequential_letters(input_string: str) -> bool:
    for i in range(len(input_string) - 2):
        # Convert the current character and the next two to their ASCII values
        first_char = ord(input_string[i])
        second_char = ord(input_string[i + 1])
        third_char = ord(input_string[i + 2])

        # Check if they form a consecutive sequence
        if second_char == first_char + 1 and third_char == second_char + 1:
            return True

    return False

def pre_process_names(names: list[str]) -> list[str]:
    return [name.lower().replace("-", "_").replace(" ", "_").strip() 
            for name in names]

def is_valid(password: str, names: list[str] | None = None) -> bool:
    match_length = len(password) >= 8
    match_lowercase_alpha = bool(re.search("[a-z]+", password))
    match_uppercase_alpha = bool(re.search("[A-Z]+", password))
    match_number_alpha = bool(re.search("[0-9]+", password))
    match_symbol = bool(re.search("[^\\w\\d]+", password))
    match_no_year = not bool(re.findall("(?:19|20)\\d{2}", password))
    match_no_sequential_letters = not check_sequential_letters(input_string=password)
    match_name =  (not any([name in password.lower() 
                            for name in pre_process_names(names=names)]) 
                        if names is not None else True)

    return (match_name and 
            match_no_sequential_letters and
            match_no_year and 
            match_length and 
            match_lowercase_alpha and 
            match_uppercase_alpha and 
            match_number_alpha and match_symbol)
