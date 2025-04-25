def eval_polynomial(poly, val):
    xs = [x.strip().replace('^', '**') for x in poly.split('+')]
    return sum([eval(n.replace('x', str(val))) for n in xs])


def run(data, x, k):
    data = data.strip()
    lines = [d for d in data.split("\n")]
    p = lines[0]
    P = eval_polynomial(p, x)
    if P == int(k):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    x, k = input().split()
    lines = ""
    for i in range(1):
        lines += input() + "\n"
    run(lines, x, k)

data = """2 15
x**5 - x - 1"""