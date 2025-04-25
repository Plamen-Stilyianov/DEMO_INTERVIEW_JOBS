import pytest
import collections


def func_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

def replicate_filter(func):
    def wrapper(col) -> list:
        result = [i for i in col if func(i)]
        return result

    return wrapper


@replicate_filter(func_even)
def find_even_numbers(col: list):
    return col


def test_replicate_filter():
    numbers = [1, 2, 3, 4, 5]
    assert find_even_numbers(numbers) == list(filter(lambda x: True if x % 2 == 0 else False, numbers))


if __name__ == '__main__':
    pytest.main(['__file__'])
