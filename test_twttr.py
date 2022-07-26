from twttr import shorten

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
    assert shorten(666) == "666"

"""
def test_numeric():
    assert shorten(666) == "666"

def test_empty():
    assert shorten("") == ""

def test_chars():
    assert shorten(".") == "."
    assert shorten("Tit.ty") == "Tt.ty"
"""