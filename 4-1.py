inp = '''
11
15
12
17
17
19
19
14
14
7
19
'''

# Find minimum of list, then sum the differences between each element and this minimum

lengths = [int(x) for x in inp.split()]

m = min(lengths)
total = 0

for l in lengths:
    total += l - m

print(total)