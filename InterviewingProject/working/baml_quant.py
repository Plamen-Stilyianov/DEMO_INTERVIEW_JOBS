# filter(lambda v: v%2 == 0, list(range(10))
def filter2(fun, col):
     return [v for v in col if fun(v)]

def even(e):
    if e%2 == 0:
        return True
    else:
        return False

g = filter2(even, [1,2,3,4,5])
if isinstance(g, list):
    print(g)
else:
    print(next(g))
    print(next(g))


def cust_filter(fun):
    def wrapper(col):
        return [x for x in col if fun(x)]
    return wrapper


@cust_filter
def even(e):
    if e%2 == 0:
        return True
    else:
        return False

@cust_filter
def odd(e):
    if e%2 != 0:
        return True
    else:
        return False

print(even([1,2,3,4,5,6]))

print(odd([1,2,3,4,5,6]))