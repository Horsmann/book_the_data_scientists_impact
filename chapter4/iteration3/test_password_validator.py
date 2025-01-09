from password_validator import is_valid

#UPDATE - new password as the previous one is now no longer permitted
def test_valid_password():
    assert is_valid(password="aK0#s7-!")

def test_reject_year_in_password():
    assert not is_valid(password="j8d-2oiS2024!")

def test_reject_lower_and_uppercased_password():
    assert not is_valid(password="abcdEFGH")

def test_reject_only_lowercased_letter_password():
    assert not is_valid(password="abcdefgh")

def test_reject_only_uppercased_letter_password():
    assert not is_valid(password="ABCDEFGH")

#NEW1 - check for no sequential letters
def test_reject_alpha_sequential_password():
    assert not is_valid(password="abcdEFGH1!")

#NEW2 - check for no sequential digits
def test_reject_digit_sequential_password():
    assert not is_valid(password="+#*5678AhiO")    
