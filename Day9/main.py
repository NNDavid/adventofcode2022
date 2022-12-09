import math
sign = lambda x: math.copysign(1, x)

def MOVE(a):
    if abs(a) <= 1:
        return 0
    elif a > 0:
        return 1
    elif a < 0:
        return -1

def MOVEDIAG(H, T):
    if abs(H[0] - T[0]) == 1 and abs(H[1] - T[1]) == 1:
        return T
    elif abs(H[0] - T[0]) == 2:
        return [T[0] + MOVE(H[0] - T[0]), T[1] + sign(H[1] - T[1])]
    elif abs(H[1] - T[1]) == 2:
        return [T[0] + sign(H[0] - T[0]), T[1] + MOVE(H[1] - T[1])]



def move(H, T):
    if H[0] == T[0]:
        return [T[0], T[1] + MOVE(H[1] - T[1])]
    elif H[1] == T[1]:
        return [T[0] + MOVE(H[0] - T[0]), T[1]]
    else:
        return MOVEDIAG(H, T)

f = open("input.txt")
rows = f.read().split('\n')
commands = [command.split(' ') for command in rows]

H = [0, 0]
T = [0, 0]
coordinates = set([tuple(T)])

for direction, s in commands:
    step = int(s)
    for i in range(step):
        if direction == 'R':
            H[1] += 1
        elif direction == 'L':
            H[1] -= 1
        elif direction == 'U':
            H[0] -= 1
        elif direction == 'D':
            H[0] += 1
        T = move(H, T)
        coordinates.add(tuple(T))

print(f"First solution {len(coordinates)}")


knots = [[0, 0] for i in range(10)]
coordinates = set([tuple(knots[9])])

for direction, s in commands:
    step = int(s)
    for i in range(step):
        if direction == 'R':
            knots[0][1] += 1
        elif direction == 'L':
            knots[0][1] -= 1
        elif direction == 'U':
            knots[0][0] -= 1
        elif direction == 'D':
            knots[0][0] += 1
        for i in range(1, 10):
            knots[i] = move(knots[i - 1], knots[i])
        coordinates.add(tuple(knots[9]))

print(f"Second solution {len(coordinates)}")