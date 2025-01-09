import re
import typing

class Rule(typing.Protocol):

    def is_complient(self, password: str) -> bool:
        ...

class LengthRule(Rule):

    def __init__(self, length: int):
        self.length = length

    def is_complient(self, password: str) -> bool:
        return len(password) >= self.length

class HasLowercasedAlphaRule(Rule):
    def is_complient(self, password: str) -> bool:
        return bool(re.search("[a-z]+", password))

class HasUppercasedAlphaRule(Rule):
    def is_complient(self, password: str) -> bool:
        return bool(re.search("[A-Z]+", password))        

class HasSymbolRule(Rule):
    def is_complient(self, password: str) -> bool:
        return bool(re.search("[^\\w\\d]+", password))

class HasNumericRule(Rule):
    def is_complient(self, password: str) -> bool:
        return bool(re.search("[0-9]+", password))

class HasNoYearRule(Rule):
    def is_complient(self, password: str) -> bool:
        return not bool(re.findall("(?:19|20)\\d{2}", password))

class HasNoSequentialCharacterRule(Rule):

    @classmethod
    def check_sequential_letters(cls, input_string: str) -> bool:
        for i in range(len(input_string) - 2):
            # Convert the current character and the next two to their ASCII values
            first_char = ord(input_string[i])
            second_char = ord(input_string[i + 1])
            third_char = ord(input_string[i + 2])

            # Check if they form a consecutive sequence
            if second_char == first_char + 1 and third_char == second_char + 1:
                return True

        return False

    def is_complient(self, password: str) -> bool:
        return not self.check_sequential_letters(input_string=password)

class HasNoNameRule(Rule):

    def __init__(self, names: list[str]):
        self.names = self.pre_process_names(names=names)

    def pre_process_names(self, names: list[str]) -> list[str]:
        return [name.lower().replace("-", "_").replace(" ", "_").strip() 
                for name in names]

    def is_complient(self, password: str) -> bool:                
        return (not any([name in password.lower() 
                for name in self.names]) 
                if self.names is not None else True)

def is_valid(password: str, rules: list[Rule]) -> bool:
    return all([rule.is_complient(password=password) for rule in rules])   
