from bank import value

def test_hello():
    assert value('Hello') == 0

def test_h():
    assert value("How are you?") == 20

def test_others():
    assert value("What's up") == 100