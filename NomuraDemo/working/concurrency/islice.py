import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = iter(numbers)
for i in range(int(len(numbers) / 3)):
    print(list(itertools.islice(iterator, 3)))
