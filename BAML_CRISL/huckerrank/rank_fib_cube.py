cube = lambda x: x * x * x  # complete the lambda function


def get_numbers(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci(n):
    # return a list of fibonacci numbers
    return [x for x in iter(get_numbers(n))]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
