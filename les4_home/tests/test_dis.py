from les4_home.tests.discrim import get_koren


def test_function():
    assert get_koren(1, -2, 1) == 1

def test_function2():
    assert get_koren(1, 2, 4) == "Нет корней"

def test_function3():
    assert get_koren(1, 3, -4) == (-4, 1)