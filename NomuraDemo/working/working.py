from math import sqrt


def run():
    count = 0
    for i, x in enumerate(range(0, 9)):
        print (i, x)

    for i, x in enumerate(range(0, int(sqrt(9)) + 1)):
        print(i, x)


if __name__ == "__main__":
    run()