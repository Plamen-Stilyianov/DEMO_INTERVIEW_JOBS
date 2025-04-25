def minion_game(string):
    # your code goes here
    s_v = ['A', 'E', 'I', 'O', 'U']
    s = str(string)
    kevin = set([])
    stuart = set([])
    for i, l in enumerate(s):
        if l in s_v:
            for j in range(len(s[i:])):
                if s[i:len(s) - j] != "":
                    kevin.add(s[i:len(s) - j])

        else:
            for j in range(len(s[i:])):
                if s[i:len(s)-j] != "":
                    stuart.add(s[i:len(s)-j])

    stu_sum = sum([s.count(w) for w in stuart])
    kev_sum = sum([s.count(w) for w in kevin])
    name = ('Stuart', stu_sum) if stu_sum > kev_sum else ('Kevin', kev_sum)
    print(f'{name[0]} {name[1]}')


if __name__ == '__main__':
    s = input()
    minion_game(s)
data = """BANANA"""