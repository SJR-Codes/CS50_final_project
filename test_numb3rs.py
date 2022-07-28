from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("10.0.0.2") == True
    assert validate("8.8.8.8") == True
    assert validate("255.254.0.254") == True

def test_invalid_ips():
    assert validate("127.0.1") == False
    assert validate("999.0.0.2") == False
    assert validate("8.8.256.8") == False
    assert validate("255.254") == False

def test_garble():
    assert validate("aaa") == False
    assert validate("balh.blah.balh.blah") == False
    assert validate("foo.bar") == False
    assert validate("") == False
    assert validate("  ") == False
