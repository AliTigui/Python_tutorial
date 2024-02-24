from main import square
import pytest

def test_negative():
    assert square(-4) == 16
    assert square(-2) == 4
    assert square(-3) == 9
def test_positive():
    assert square(4) == 16
    assert square(2) == 4
    assert square(3) == 9
def test_zero():
    assert square(0) == 0
def test_error():
    with pytest.raises(TypeError):
        square("cat")

