"""
* CS50P Problem Set 7
* Test Working 9 to 5
* by Samu Reinikainen 28.07.2022
"""

import pytest
from working import convert

def test_valid_times():
    assert convert("09:00 AM to 05:00 PM") == "9:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("9 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("12 AM to 5:00 PM") == "00:00 to 17:00"
    assert convert("8:35 AM to 4:45 PM") == "8:35 to 16:45"


def test_invalid_times():
    with pytest.raises(ValueError):
        assert convert("09:70 AM to 05:00 PM")
    with pytest.raises(ValueError):
        assert convert("09:00 to 05:00 PM")
    with pytest.raises(ValueError):
        assert convert("09:00 AM to 05:00")
    with pytest.raises(ValueError):
        assert convert("09:00 AM to")


def test_garble():
    with pytest.raises(ValueError):
        assert convert("huuhaa")
    with pytest.raises(ValueError):
        assert convert("foo AM to bar PM")
    with pytest.raises(ValueError):
        assert convert(" ")
