"""
* CS50P Problem Set 8
* Test Cookie Jar
* by Samu Reinikainen 30.07.2022
"""

import pytest
import jar

def test_init():
    with pytest.raises(ValueError):
        pot = jar.Jar(-1)
    with pytest.raises(ValueError):
        pot = jar.Jar("gaa")

def test_deposit():
    pot = jar.Jar(5)
    with pytest.raises(ValueError):
        pot.deposit(-5)
    with pytest.raises(ValueError):
        pot.deposit("10")
    with pytest.raises(ValueError):
        pot.deposit("guu")

def test_withdraw():
    pot = jar.Jar(3)
    with pytest.raises(ValueError):
        pot.withdraw(-5)
    with pytest.raises(ValueError):
        pot.withdraw("10")
    with pytest.raises(ValueError):
        pot.withdraw("guu")

def test_print():
    pot = jar.Jar(12)
    pot.deposit(1)
    assert pot.__str__() == "🍪"
    pot.withdraw(1)
    assert pot.__str__() == ""
    pot.deposit(5)
    assert pot.__str__() == "🍪🍪🍪🍪🍪"

def test_capacity():
    pot = jar.Jar(1)
    assert pot.capacity == 1
    pot = jar.Jar(5)
    assert pot.capacity == 5
    pot = jar.Jar()
    assert pot.capacity == 12

def test_size():
    pot = jar.Jar(12)
    assert pot.size == 0
    pot.deposit(5)
    assert pot.size == 5
    pot.deposit(7)
    assert pot.size == 12