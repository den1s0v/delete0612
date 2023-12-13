from calculator import divide


def run():
    assert 2 == divide(10, 5)
    assert 5 == divide(10, 2)
    assert 0 == divide(0, 2)
    assert 0 == divide(2, 0)
    assert 0 == divide(0, 0)
