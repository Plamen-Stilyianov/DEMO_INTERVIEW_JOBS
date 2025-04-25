import pytest
from unittest.mock import Mock

count_calls = Mock()
count_calls.counter = 0


def count_func_calls():
    count_calls.counter += 1


class cache:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


@cache
def cube(num):
    count_func_calls()
    return num ** 3


@pytest.mark.parametrize("nums, expected", [([2, 3, 4, 5, 5, 6, 5], 5)])
def test_cube(nums, expected):
    list(map(cube, nums))
    assert count_calls.counter == expected


if __name__ == '__main__':
    pytest.main([__file__])
