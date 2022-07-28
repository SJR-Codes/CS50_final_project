"""
* CS50P Problem Set 7
* Test Working 9 to 5
* by Samu Reinikainen 28.07.2022
"""

import pytest
from um import count

def test_simple():
    assert count("um") == 1
    #this needs more studying
    #assert count("um um") == 2
    assert count("ummu") == 0
    assert count("Regular, um, Expressions") == 1
    assert count("Regular, um, um, Expressions") == 2
    assert count("Regular, UM, Um, Expressions um...") == 3
    assert count("It’s um not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!") == 3


def test_um_in():
    assert count("Regular yummy Expressions") == 0
    assert count("Um... Regular yummy Expressions") == 1
    assert count("Regular Mum Expressions") == 0
    assert count("Regular Mum Expressions ...um") == 1
    assert count("Regular, um, mum, Expressions") == 1

def test_garble():
    assert count(" ") == 0
    assert count("1234um435") == 0
    assert count("1234 um, 435") == 1
    assert count("1234 (um) 435") == 1

def test_multiline():
    assert count(
            "It’s um not uncommon, in English, at least,\n\
            to say “um” when trying to, um, think of a word.\n\
            The more you do it, though, the more noticeable it tends to be!") == 3
