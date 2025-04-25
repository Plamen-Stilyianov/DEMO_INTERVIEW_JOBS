
def f(*t):
    if len(t) == 0:
        return 0
    elif len(t) == 1:
        a = t[0]
        b = 0
        z = 0
    elif len(t) == 2:
        a = t[0]
        b = t[1]
        z = 0
    elif len(t) == 3:
        a, b, z = t
    else:
        return 0
    return a + b - z

if __name__ == "__main__":
    print(f())
    print(f(2, 3))
    print(f(2,3,4,5))