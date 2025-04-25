import multiprocessing as mp
from math import sqrt


def is_prime(num):
    # determine whether num is prime
    isp = False
    # prime numbers are greater than 1

    # check for factors
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if (num % i) == 0:
                # if factor is found, set flag to True
                isp = False
                # break out of loop
                break
        else:
            isp = True
    return (num, isp)


if __name__ == '__main__':

    # create a pool with cpu_count() procs.
    pl = mp.Pool()
    results = pl.map(is_prime, range(0, 9))
    for num, isp in results:
        if isp:
            print( num, " is prime" )
