import re

def validate_number(line):
    if len(line) == 10:
        for l in line:
            if not l.isdigit():
                return 'NO'
        return 'YES' if bool(re.match(r'(^[987].?(\d+))', line)) else 'NO'
    else:
        return 'NO'


if __name__ == "__main__":
    lines = []
    for _ in range(int(input())):
        lines.append(input())

    for line in lines:
        print(validate_number(line))

data = """3
8F54698745
9898959398
879546242"""
