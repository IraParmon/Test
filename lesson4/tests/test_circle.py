from math import pi

import pytest

from lesson4.circle import get_square


def test_circle():
    assert get_square(1) == pi


def test_sub():
    with pytest.raises(Exception):
        get_square(0)
