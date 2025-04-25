s = 'Boomberg'
i = s.index('B')
l_str = [l for l in s]
l_str.insert(i+1,'l')
s = ''.join(l_str)
print(s)