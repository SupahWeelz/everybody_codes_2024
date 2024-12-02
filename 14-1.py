inp='U101,L1,U1,F1,U1,R1,U1,L1,B1,F1,L1,F1,U1,L1,U3,L1,R1,F2,U3,L1,U2,L1,U4,L1,U1,B1,F1,B1,R1,B1,L1,F1,U3,L2,U1,L1,U1,B1,R1,U1,F1,U2,B1,U1,R1,U3,R1,U1,R1,F1,U2,F1,U3,R1,F1,U1,F1,U1,F1,L3,B1,U2,F1,D1,F2,U1,F1,U1,D1,U2,B1,D1,L1,U1,L1,D1,B1,F1,L1,U1,R1,B1,F1,U1,D1,U2,B1,R2,U2,D1,U1,L1,U1,D1,L1,D1,F2,U1,R1,U2,B1,D1,L1,F1,D1,U2,R1,U1,R1,D1,U1,D3,U1,B1,U4,D1,L1,D1,U1,B1,D1,B1,F1,R1,D1,R2,D1,F2,B2,D2,L1,U1,R1,U1,D2,F2,D1,R1,F2,D5'

directions = inp.split(',')
maxHeight = 0
curHeight = 0

for d in directions:
    dir, mag = d[0], int(d[1:])
    if dir == 'U':
        curHeight += mag
        if curHeight > maxHeight:
            maxHeight = curHeight
    elif dir == 'D':
        curHeight -= mag

print(maxHeight)