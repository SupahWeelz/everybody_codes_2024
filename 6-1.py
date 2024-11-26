inp='''
HK:PT,TJ
LH:FC,@
GN:WM,DJ
HQ:DV,FF
PW:CF
LM:WH,ZC
JD:RH,NN
SP:RL,BJ,@
FZ:HK
FF:BB,RG
RL:@
TJ:PH
SN:KM,QL
BK:WJ,JZ
PH:BK,ML
RM:CN,LH,@
JQ:RM
QM:SP,GN,@
FC:SN,MV,@
PT:NP
ND:MH,HX
RR:JQ,TZ,FZ
CN:QM,@
NP:ND,WX
DV:JJ,KQ
VN:PW,LX,@
BJ:@
MV:MD,FD
WX:PG,CC
CF:JD,LM
TZ:VN
LX:HQ
ML:GR,HB
'''

# Count length from each fruit to the root
# Store path like so: {[@, br1, br2, ...]: length}

tree = inp.split()
dic = {}
for element in tree:
    [key, value] = element.split(':')
    value = tuple(value.split(','))
    key, value = value, key
    dic[key] = value

for d in dic:
    length = 0
    if '@' in d:
        curr = dic[d]
        path = [curr]
        while curr != 'RR':
            for d_ in dic:
                if curr in d_:
                    curr = dic[d_]
                    length += 1
                    path.append(curr)
        print(*path[::-1], length)
