from password_validator import (
    is_valid, 
    LengthRule, 
    HasLowercasedAlphaRule, 
    HasUppercasedAlphaRule, 
    HasSymbolRule, 
    HasNoNameRule, 
    HasNoSequentialCharacterRule, 
    HasNoYearRule, 
    HasNumericRule
)

def test_length_rule():
    rule = LengthRule(length=8)
    assert rule.is_complient(password="12345678")
    assert not rule.is_complient(password="1234567")

def test_numeric_rule():
    rule = HasNumericRule()
    assert rule.is_complient(password="12345678")
    assert not rule.is_complient(password="abcdef")

def test_has_lowercased_alpha_rule():
    rule = HasLowercasedAlphaRule()
    assert rule.is_complient(password="1a")
    assert not rule.is_complient(password="1A")

def test_has_uppercased_alpha_rule():
    rule = HasUppercasedAlphaRule()
    assert rule.is_complient(password="1A")
    assert not rule.is_complient(password="1a")

def test_has_symbol_rule():
    rule = HasSymbolRule()
    assert rule.is_complient(password="1A+")    
    assert not rule.is_complient(password="1a")

def test_has_no_name_rule():
    rule = HasNoNameRule(names=["judith"])
    assert rule.is_complient(password="1a")
    assert not rule.is_complient(password="1ajudith")

def test_has_no_sequential_character_rule():
    rule = HasNoSequentialCharacterRule()
    assert rule.is_complient(password="a-b-c")
    assert not rule.is_complient(password="abc")

def test_has_no_year_rule():
    rule = HasNoYearRule()
    assert rule.is_complient(password="+fAjf9")
    assert not rule.is_complient(password="ab2020+")

def test_is_valid():
    rules = [HasNumericRule(), HasLowercasedAlphaRule(), 
             HasUppercasedAlphaRule()]
    assert is_valid(password="1aB", rules=rules)
    assert not is_valid(password="1a", rules=rules)
    assert not is_valid(password="1A", rules=rules)
    assert not is_valid(password="a", rules=rules)

