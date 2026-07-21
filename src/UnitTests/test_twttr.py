from twttr import shorten

def test_shorten():
    assert shorten('Hello') == 'Hll'
    assert shorten('Twitter') == 'Twttr'
    assert shorten('M3SSI') == 'M3SS'
    assert shorten('Hello!') == 'Hll!'