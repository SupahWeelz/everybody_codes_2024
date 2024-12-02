inp=446
mod=1111
st=3
tgt=20240000
tot=1

def rng():
    init = 1
    while True:
        init = (init * inp) % mod
        yield init

g = rng()

while tot < tgt:
    tot += st * next(g)
    st += 2

print((tot - tgt) * (st - 2))