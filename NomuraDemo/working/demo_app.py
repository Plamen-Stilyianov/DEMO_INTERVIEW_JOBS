def passing(l):
    l[1].append('fjk')


def run():
    l = (['abc'], ['cde'])
    passing(l)
    print(l)

if __name__ == "__main__":
    run()
