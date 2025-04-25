from collections import Counter
def run(lines):
    print(len(set(lines)))
    for v in Counter(lines).values():
        print(v, end=" ")


if __name__ == "__main__":
    n = input()
    lines = []
    for i in range(int(n)):
        lines.append(input())
    run(lines)
data = """4
bcdef
abcdefg
bcde
bcdef"""