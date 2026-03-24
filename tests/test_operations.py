from src.math_operation import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(8, 8) == 0
