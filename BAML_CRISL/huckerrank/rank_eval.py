def run(data):
    data = data.replace('print(', '')[:-1]
    print(eval(data))


if __name__ == "__main__":
    run(input())

data = """print(abs(-1)-1)"""