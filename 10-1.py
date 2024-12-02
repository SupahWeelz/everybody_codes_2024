inp='''
**GFCD**
**VHTN**
MV....PJ
XZ....SK
HW....NC
FD....TG
**WSPJ**
**XMZK**
'''

dat = [list(x) for x in inp.split()]

print(dat)

import numpy as np

dat = np.array(dat)

horis, verts = [], []

for i in range(2, 6):
    horizontal = ''
    for j in range(len(dat)):
        if dat[i][j] != '.':
            horizontal += dat[i][j]
    horis.append(horizontal)

    vertical = ''
    for j in range(len(dat)):
        if dat[j][i] != '.':
            vertical += dat[j][i]
    verts.append(vertical)

ans = ''

for h in horis:
    for v in verts:
        h_ = set(h)
        v_ = set(v)
        ans += list(h_.intersection(v_))[0]

print(ans)