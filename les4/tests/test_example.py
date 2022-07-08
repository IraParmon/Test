from les4.my_function import month


def test_my_function():
    assert month(1) == 31


def test_my_function1():
    assert month(2) == 'ФЕВРАЛЬ!'


def test_my_function2():
    assert month(3) == 30
