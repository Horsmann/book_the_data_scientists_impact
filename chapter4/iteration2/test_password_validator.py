from password_validator import is_valid

#NEW1 - valid password
def test_valid_password():
    assert is_valid(password="abcdEFGH1!")

#NEW2 - no password with the year 2024 in it
def test_reject_year_in_password():
    assert not is_valid(password="j8d-2oiS2024!")

#UPDATE - valid in previous example, now invalid
def test_reject_lower_and_uppercased_password():
    assert not is_valid(password="abcdEFGH")

def test_reject_only_lowercased_letter_password():
    assert not is_valid(password="abcdefgh")

def test_reject_only_uppercased_letter_password():
    assert not is_valid(password="ABCDEFGH")    
