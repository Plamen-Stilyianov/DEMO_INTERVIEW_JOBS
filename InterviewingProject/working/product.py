import numpy as np
def prod(a, b):
    prod = [abs(a) for _ in range(abs(b))]  # [a] * abs(b)
    return sum(prod) if ((a < 0 and b < 0) or (a > 0 and b > 0)) else -sum(prod)

def num_prod(a, b):
    prod = np.array([a,b])
    return np.prod(prod)

def main():
    print(f' -3 * -5 {-3 * -5} : {prod(-3, -5)}')
    print(f' -3 * 5 {-3 * 5} : {prod(-3, 5)}')
    print(f' 3 * 5 {3 * 5} : {prod(3, 5)}')
    print(f' 3 * -5 {3 * -5} : {prod(3, -5)}')
    print(f' ==================================== ')
    print(f' -3 * -5 {-3 * -5} : {num_prod(-3, -5)}')
    print(f' -3 * 5 {-3 * 5} : {num_prod(-3, 5)}')
    print(f' 3 * 5 {3 * 5} : {num_prod(3, 5)}')
    print(f' 3 * -5 {3 * -5} : {num_prod(3, -5)}')


if __name__ == '__main__':
    main()
