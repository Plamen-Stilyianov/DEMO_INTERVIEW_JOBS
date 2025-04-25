def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

def closure():
    times4 = make_multiplier_of(4)
    print(f'{4 * 3} == {times4(3)}')


if __name__ == '__main__':
    closure()