"""
* CS50P Problem Set 8
* Test Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

import pytest
from seasons import dates_to_minutes, sing_minutes

def test_d2m_valid():
    assert dates_to_minutes("2021-07-29", "2022-07-29") == 525600
    assert dates_to_minutes("2020-07-29", "2022-07-29") == 1051200

def test_d2m_invalid():
    with pytest.raises(SystemExit):
        assert dates_to_minutes("1999-05-35", "2022-07-29")
    with pytest.raises(SystemExit):
        assert dates_to_minutes("1999-05-", "2022-07-29")
    with pytest.raises(SystemExit):
        assert dates_to_minutes("aaaa-bb-cc", "2022-07-29")

def test_sing():
    assert sing_minutes(525600) == "Five hundred twenty-five thousand, six hundred minutes."
    assert sing_minutes(1051200) == "One million fifty-one thousand, two hundred minutes."

def test_sing_fail():
    with pytest.raises(SystemExit):
        assert sing_minutes("aaa")
    with pytest.raises(SystemExit):
        assert sing_minutes("")
