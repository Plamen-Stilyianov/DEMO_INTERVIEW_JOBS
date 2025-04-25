from collections import deque


def is_palindomic(n):
    if n < 10:
        return True
    else:
        dq = deque(str(n))
        for i in range(int(len(dq) / 2)):
            if dq.popleft() == dq.pop():
                if len(dq) < 2:
                    return True
                else:
                    return False
            else:
                return False


def run(data):
    q1 = [x > 0 for x in data]
    if not all(q1):
        print(False)
    else:
        q2 = [is_palindomic(x) for x in data]
        if any(q2):
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    nm = input()
    arr = []

    for _ in range(1):
        arr.append(list(map(lambda x: int(x), input().rstrip().split())))
    run(arr[0])
data="""5
12 9 61 5 14"""