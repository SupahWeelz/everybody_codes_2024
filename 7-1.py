inp='''
F:=,+,-,=,=,+,+,-,-,+
H:+,+,-,+,=,-,=,+,=,-
A:+,+,-,=,=,+,=,+,-,-
E:+,=,-,-,-,+,+,=,=,+
B:+,+,-,=,+,=,+,-,=,-
G:-,=,+,-,-,+,=,+,=,+
I:+,=,+,-,=,=,+,-,-,+
C:-,-,=,-,+,+,=,=,+,+
J:=,-,=,+,+,+,-,-,+,=
'''

def simulate(plan):
    start = 10
    total = 0
    for p in plan:
        if p == '-':
            start -= 1
        elif p == '+':
            start += 1
        total += start
    return total

plans = inp.split()
planDict = {}
for p in plans:
    key, value = p.split(':')
    value = value.split(',')
    planDict[key] = value

results = {}

for p in planDict:
    total = simulate(planDict[p])
    results[p] = total

results = dict(sorted(results.items(), key=lambda item: item[1])[::-1])

for r in results:
    print(r, end='')