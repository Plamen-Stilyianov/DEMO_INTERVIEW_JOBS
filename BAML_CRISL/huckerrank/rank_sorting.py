def run(data):
    lower = []
    upper = []
    digits = []
    for i in data:
        if str(i).isalpha() and str(i).islower():
            lower.append(i)
        elif str(i).isalpha() and str(i).isupper():
            upper.append(i)
        else:
            digits.append(i)
    lower.sort()
    upper.sort()
    digits.sort(key=lambda x: (-(int(x) % 2), int(x)))
    lower.extend(upper)
    lower.extend(digits)
    return "".join(lower)


if __name__ == '__main__':
    line = input()
    print(run(line))
data = 'Sorting1234'
