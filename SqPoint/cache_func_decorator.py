import pytest
from unittest.mock import Mock

count_calls = Mock()
count_calls.counter = 0


def count_func_calls():
    count_calls.counter += 1


def cache(func):
    cache_data = {}

    def wrapper_func(num):
        key = str(num) + str(num.__hash__())
        if key in cache_data:
            return cache_data[key]
        else:
            value = func(num)
            cache_data[key] = value
        return value

    return wrapper_func


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
