from password_validator import (
    is_valid, 
    LengthRule, 
    HasLowercasedAlphaRule, 
    HasUppercasedAlphaRule, 
    HasSymbolRule, 
    HasNoNameRule, 
    HasNoSequentialCharacterRule, 
    HasNoYearRule, 
    HasNumericRule)

rules = [LengthRule(length=8), 
         HasLowercasedAlphaRule(), 
         HasUppercasedAlphaRule(), 
         HasSymbolRule(), 
         HasNoNameRule(names=["Petra", "Sven", "Anna Lena", "Jean-Luc"]), 
         HasNoSequentialCharacterRule(), 
         HasNoYearRule(), 
         HasNumericRule()]


def test_valid_password():
    assert is_valid(password="aK0#s7-!", rules=rules)

def test_reject_year_in_password():
    assert not is_valid(password="j8d-2oiS2024!", rules=rules)

def test_reject_lower_and_uppercased_password():
    assert not is_valid(password="abcdEFGH", rules=rules)

def test_reject_only_lowercased_letter_password():
    assert not is_valid(password="abcdefgh", rules=rules)

def test_reject_only_uppercased_letter_password():
    assert not is_valid(password="ABCDEFGH", rules=rules)

def test_reject_alpha_sequential_password():
    assert not is_valid(password="abcdEFGH1!", rules=rules)

def test_reject_digit_sequential_password():
    assert not is_valid(password="+#*5678AhiO", rules=rules)

def test_reject_name_in_password():
    assert not is_valid(password="+#*hFsven9-fi", rules=rules)
