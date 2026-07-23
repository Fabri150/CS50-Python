from plates import is_valid

def test_validstart():
    assert is_valid("1CS50") is False
    assert is_valid("A123") is False

def test_firstzero():
    assert is_valid("AEI012") is False

def test_validlen():
    assert is_valid("AEI0123") is False
    assert is_valid("A") is False

def test_validnumber():
    assert is_valid("AAA22A") is False
    assert is_valid("AAA022") is False
    assert is_valid("AAA222") is True

def test_checkpunctuation():
    assert is_valid("AA!22") is False
    assert is_valid("AA 22") is False
