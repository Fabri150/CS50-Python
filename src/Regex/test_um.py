from um import count

def test_count():
    assert count("um") == 1

def test_um_suffix():
    assert count("um?") == 1
    assert count("um...") == 1

def test_um_substring():
    assert count("yummy") == 0

def test_phrase_with_um():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2