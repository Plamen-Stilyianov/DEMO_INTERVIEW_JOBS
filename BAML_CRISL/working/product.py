import pytest


def prod(a: int, b: int) -> int:
    prod_l = [abs(a) for _ in range(abs(b))]
    return sum(prod_l) if ((a < 0 and b < 0) or (a > 0 and b > 0)) else -sum(prod_l)


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-3, -4, 12),
    (-3, 4, -12),
    (3, -4, -12),
])
def test_prod(a: int, b: int, expected: int) -> None:
    assert prod(a, b) == expected


if __name__ == '__main__':
    pytest.main([__file__])
