from collections import deque


def run(s, leftShift, rightShift):
    shift = rightShift - leftShift
    dq = deque(s)
    if shift > 0:
        for i in range(shift):
            dq.append(dq.popleft())
    elif shift < 0:
        for i in range(abs(shift)):
            dq.appendleft(dq.pop())
    else:
        dq = dq

    return "".join([""+i for i in dq])


if __name__ == "__main__":
    s = 'plamen.stilyianov'
    leftShift=4
    rightShift=3
    print(run(s, leftShift, rightShift))

