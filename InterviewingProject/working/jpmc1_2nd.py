from collections import Counter

def run(l):
    freq = Counter(l)
    idx, fr = freq.most_common()[0]
    print(f'The max frequency is {fr} of number {idx} ')

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 5, 6, 7, 3, 4]
    run(l)
