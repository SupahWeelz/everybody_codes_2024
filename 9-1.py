inp='''
10059
11680
16636
10099
17887
17244
14402
17865
10107
10000
'''

lums = [int(x) for x in inp.split()]

stamps = [10, 5, 3, 1]

total = 0

for lum in lums:
    for s in stamps:
        t = lum // s
        total += t
        lum -= s * t
        print(lum, total)

print(total)