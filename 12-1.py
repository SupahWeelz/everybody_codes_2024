inp='''
.................................
.C............T.......T..T.T...T.
.B............T.......T..T.T...T.
.A............T.......T..T.T...T.
=================================
'''

distances = [13, 21, 24, 26, 30]

total = 0

for d in distances:
    toMult = d // 3
    additional = d % 3
    total += toMult * 6
    if additional == 1:
        total += 1
    elif additional == 2:
        total += 3

print(total)