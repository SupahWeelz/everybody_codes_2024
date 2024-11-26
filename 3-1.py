inp = '''
..............................
.............#................
.............##...............
.............##...##..........
........####..###.##..........
.........##########...........
........#############.........
........#############.........
.......############.#.........
.......##..#..###.............
...........##..#..............
..............................
..............................
..............................
'''

# Go through until there are no more # left
# First iteration, check all # adjacent to .
# Second iteration, check all # adjacent to 1
# Third iteration, check all # adjacent to 2
# etc.

def dig():
    toCheck = '.'
    k = 1
    total = 0
    while any('#' in sublist for sublist in matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '#':
                    neighbors = [matrix[i][j+1], matrix[i][j-1], matrix[i+1][j], matrix[i-1][j]]
                    for n in neighbors:
                        if n == toCheck:
                            matrix[i][j] = k
                            total += k
                            break

        toCheck = k
        k += 1
    return total


field = inp.split()
length = len(field[0])
height = len(field)

matrix = [ [0] * length for i in range(height) ]

for i in range(len(field)):
    for j in range(len(field[i])):
        sym = field[i][j]
        matrix[i][j] = sym

ans = dig()

for m in matrix:
    print(*m)

print(ans)