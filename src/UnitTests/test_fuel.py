import pytest
from fuel import convert
from fuel import gauge
    
def test_convert():
    assert convert('1/2') == 50
    with pytest.raises(ValueError):
        convert('x/1')
    with pytest.raises(ValueError):
        convert('-2/-1')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'