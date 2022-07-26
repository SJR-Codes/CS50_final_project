from twttr import shorten
import pytest

def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Tweet") == "Twt"

def test_words_with_y():
    assert shorten("Titty") == "Ttty"
    assert shorten("Tweety") == "Twty"

def test_words_upper():
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("TwEEt") == "Twt"

def test_words_with_y_uppper():
    assert shorten("TIttY") == "TttY"
    assert shorten("TweEtY") == "TwtY"

def test_numeric():
    with pytest.raises(TypeError):
        assert shorten(666)

def test_empty():
    with pytest.raises(TypeError):
        assert shorten()