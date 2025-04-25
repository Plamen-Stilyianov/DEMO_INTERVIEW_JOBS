from concurrent.futures import ThreadPoolExecutor
import threading
import random


def task():
    print("Executing our Task")
    result = 0
    for i in range(10):
        result += random.randint(0,1)
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)


if __name__ == '__main__':
    main()
