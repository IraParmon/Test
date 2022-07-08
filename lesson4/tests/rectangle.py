import pytest
from lesson4.rectangle import get_square3, get_perim3


def test_recatngle():
    assert get_square3(2, 2) == 4

def test_recatngle2():
    assert get_perim3(2, 2) == 4


def test_sub2():
    with pytest.raises(Exception):
        get_square2(0,1)