from collections import Counter

def run(s):
    counter = Counter(s)
    counts = sorted(counter.items(), key=lambda item: (-int(item[1]), item[0]))
    [print(f"{item[0]} {item[1]}") for item in counts[:3]]


if __name__ == "__main__":
    s = input()
    run(s)

data = 'qwertyuiopasdfghjklzxcvbnmq'