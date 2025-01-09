from password_validator import is_valid

def test_valid_password():
    assert is_valid(password="abcdEFGH")

def test_reject_only_lowercased_letter_password():
    assert not is_valid(password="abcdefgh")

def test_reject_only_uppercased_letter_password():
    assert not is_valid(password="ABCDEFGH")      
