"""
* CS50P Problem Set 5
* Test Vanity Plates
* by Samu Reinikainen 26.07.2022
"""

from plates import is_valid

def test_str_lenghth():
    assert is_valid("AAAAAA") == True
    assert is_valid("AA") == True
    assert is_valid("AAAAAAAA") == False
    assert is_valid("A") == False

def test_str_first_chars():
    assert is_valid("AAAAAA") == True
    assert is_valid("AA123") == True
    assert is_valid("12AA") == False
    assert is_valid("0A") == False
    assert is_valid("100") == False

def test_not_alphanum_chars():
    assert is_valid("AAAAAA") == True
    assert is_valid("AA123") == True
    assert is_valid("AA++AA") == False
    assert is_valid("🙂🙂🙂") == False

def test_nums_last():
    assert is_valid("AAA100") == True
    assert is_valid("AAA111") == True
    assert is_valid("AAA07A") == False
    assert is_valid("AA0A07") == False
    assert is_valid("AA7A77") == False

def test_no_zero_first():
    assert is_valid("AAA100") == True
    assert is_valid("AAA007") == False