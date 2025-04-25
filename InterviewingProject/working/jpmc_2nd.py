from numpy import prod

def run(l):
    product = {}
    for i in l[1:-1]:
        for j in l:
            if i == j:
                continue
            if i not in product:
                product[i] = int(prod([i, j]))
            elif i in product:
                if product[i] < prod([i, j]):
                    product[i] = int(prod([i, j]))
    l_sorted = sorted(product.items(), key=lambda x: x[1], reverse=True)
    return l_sorted[0][1]


if __name__ == '__main__':
    l = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    print(run(l))
