from lesson4.triangle import get_square2, get_perim2
import pytest

def test_triangle():
    assert get_square2(5, 5, 5) == 10.825317547305483

def test_triangle2():
    assert get_perim2(5, 5, 5) == 15

def test_sub1():
    with pytest.raises(Exception):
        get_square2(0,1,1)
