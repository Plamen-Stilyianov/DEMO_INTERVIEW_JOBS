import re


def print_match(s, p):
    m = re.search(p, s)
    pattern = re.compile(p)
    if not m:
        print('(-1, -1)')
    else:
        while m:
            print('{}, {}'.format(m.start(), m.end() - 1))
            m = pattern.search(s, m.start() + 1)


if __name__ == "__main__":
    string = 'aaadaa'  # input()
    pattern = 'aa'  # input()
    print_match(string, pattern)
