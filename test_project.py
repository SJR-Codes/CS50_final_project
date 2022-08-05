"""
* CS50P Final Project
* Test Final Project Representer
* by Samu Reinikainen 05.08.2022
"""
import pytest
from project import get_image, get_script, say



def test_get_image():
    with pytest.raises(TypeError):
        assert get_image()
    assert get_image("") == None
    assert get_image("foo") == False
    assert get_image("test.png") != False


def test_get_script():
    with pytest.raises(TypeError):
        assert get_script()
    assert get_script("") == None
    with pytest.raises(SystemExit):
        assert get_script("foo")
    with pytest.raises(SystemExit):
        assert get_script("test.png")
    with pytest.raises(SystemExit):
        assert get_script("invalid_script.txt")
    assert get_script("script.txt") != False

def test_say():
    with pytest.raises(TypeError):
        assert say()
    with pytest.raises(SystemExit):
        engine = ""
        assert say(engine, "Hey")