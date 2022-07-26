from bank import value

def test_100():
    assert value("  Hello") == 100
    assert value("Yello") == 100

def test_20():
    assert value("Hi") == 20
    assert value("How are you") == 20

def test_0():
    assert value("Hello") == 0
    assert value("Hello, sir") == 0

def test_100_low():
    assert value("  hello") == 100
    assert value("yello") == 100

def test_20_low():
    assert value("hi") == 20
    assert value("how are you") == 20

def test_0_low():
    assert value("hello") == 0
    assert value("hello, sir") == 0

def test_100_numeric():
    assert value(50) == 100
    assert value(666) == 100