# Problem Name is &&& Pascals Triangle &&& PLEASE DO NOT REMOVE THIS LINE.

"""

  The below pattern of numbers are called Pascals Triangle.

  Pascals Triangle exhibits the following behaviour:

  The first and last numbers of each row in the triangle are 1
  Each number in the triangle is the sum of the two numbers above it.

  Example:
               1
              1 1
             1 2 1
            1 3 3 1
           1 4 6 4 1
         1 5 10 10 5 1
        1 6 15 20 15 6 1

  Please Complete the 'pascal' function below so that given a
  col and a row it will return the value in that positon.

  Example, pascal(1,2) should return 2

"""


def pascal(col, row):
    rowValmap = {}

    for c in range(col + 1):  # c = 2
        for r in range(row + 1):  # len = [0,1,2]
            rowValmap[(c, r)] = 1 + r if c == r == 0 else r
        print("{} : {}".format(col, row))

    for key, val in rowValmap.items():
        print("{} : {}".format(key, val))

    return rowValmap[(col,row)]


def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    doPass = True
    pascalColRowValues = {(0, 0): 1, (1, 2): 2, (5, 6): 6}

    for key, val in pascalColRowValues.items():
        if pascal(key[0], key[1]) != val:
            doPass = False
            print("Failed for {} and {} \n".format(key, val))

    if doPass:
        print("All tests pass\n")

    return doPass


if __name__ == "__main__":
    doTestsPass()