inp=4098234

st = 1
tot = 0

while tot < inp:
    tot += st
    st += 2

print(tot, inp, st - 2)

print((tot - inp) * (st - 2))