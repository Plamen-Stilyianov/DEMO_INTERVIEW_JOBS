import re

if __name__ == "__main__":
    [print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input())) for _ in range(int(input()))]

data = """11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides."""
