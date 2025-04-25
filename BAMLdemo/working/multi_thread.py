# pool will get bad result since GIL
import time
from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)


def profile(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        s = time.time()
        func(*args, **kwargs)
        e = time.time()
        print("cost: {0}".format(e - s))

    return wrapper


@profile
def pool_map():
    res = pool.map(lambda x: x ** 2, range(999999))


@profile
def ordinary_map():
    res = map(lambda x: x ** 2, range(999999))


pool_map()
ordinary_map()
