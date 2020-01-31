from adder import simple_adder


def test_positive_numbers():
    assert simple_adder(4, 5) == 9


def test_negative_numbers():
    assert simple_adder(-3, -7) == -10


def test_zero():
    assert simple_adder(4, 0) == 4
