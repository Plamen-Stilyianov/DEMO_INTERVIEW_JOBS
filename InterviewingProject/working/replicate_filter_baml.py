import pytest


def rep_filter(func, col):
    return [el for el in col if func(el)]


def even(el):
    return True if el % 2 == 0 else False


def test_rep_filter():
    assert rep_filter(even, list(range(1, 11))) == list(filter(lambda x: x % 2 == 0, list(range(1, 11))))


if __name__ == "__main__":
    pytest.main([__file__])
