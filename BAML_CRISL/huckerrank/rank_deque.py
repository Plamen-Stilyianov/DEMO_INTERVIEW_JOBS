from collections import deque


def run(data):
    dq = deque()
    for k, v in data:
        f = getattr(dq, k)
        if v is None:
            f()
        else:
            f(v)
    [print(x, end=' ') for x in dq]


if __name__ == "__main__":
    n = input()
    commands = []
    for i in range(int(n)):
        line = input().split(' ')
        value = int(line[1]) if len(line) > 1 else None
        commands.append((line[0], value))
    run(commands)
data = """6
append 1
append 2
append 3
appendleft 4
pop
popleft"""
