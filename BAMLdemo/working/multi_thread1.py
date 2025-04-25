import unittest
from multiprocessing.pool import ThreadPool


def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)



def run_threads():
    ''' Testing thread safety of the methods of the anagram class instance '''
    pool = ThreadPool(processes=1)
    async_result_f5 = pool.apply_async(fib, len((1,2,3,4,5)))
    unittest.TestCase.assertEqual(8, async_result_f5.get())


if __name__ == "__main__":
    run_threads()