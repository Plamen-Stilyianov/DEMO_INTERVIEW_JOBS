# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


def validate(stack):
    for i in range(len(stack) - 1):
        if stack[0] < stack[1]:
            return 'No'
        stack.popleft()
    return 'Yes'


def run(lines):
    for line in lines:
        n = int(line[1])
        dq = deque(line[0])
        stack = deque()
        for i in range(n):
            if len(dq) == 1:
                stack.append(int(dq.pop()))
            else:
                if int(dq[0]) >= int(dq[-1]):
                    stack.append(int(dq.popleft()))
                else:
                    stack.append(int(dq.pop()))

        print(validate(stack))


if __name__ == "__main__":
    n = input()
    lines = []
    for i in range(int(n)):
        line_1 = input()
        line_2 = input().split(' ')
        lines.append((line_2, line_1))
    run(lines)

data = """"2
6
4 3 2 1 3 4
3
1 3 2"""
