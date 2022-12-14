def printCave(cave):
    for row in cave:
        print("".join(row))


def simulateSand(start, cave):
    rows = len(cave)
    cols = len(cave[0])
    coordinate = start
    while True:
        next_coordinate = (coordinate[0] + 1, coordinate[1])
        if next_coordinate[0] not in range(rows) or next_coordinate[1] not in range(cols):
            break
        if cave[next_coordinate[0]][next_coordinate[1]] != '.':
            if cave[next_coordinate[0]][next_coordinate[1] - 1] == '.':
                next_coordinate = (next_coordinate[0], next_coordinate[1] - 1)
            elif cave[next_coordinate[0]][next_coordinate[1] + 1] == '.':
                next_coordinate = (next_coordinate[0], next_coordinate[1] + 1)
            else:
                return coordinate
        coordinate = next_coordinate
    return None


def simulateSand2(start, cave):
    rows = len(cave)
    cols = len(cave[0])
    coordinate = start
    while True:
        next_coordinate = (coordinate[0] + 1, coordinate[1])
        if next_coordinate[0] not in range(rows) or next_coordinate[1] not in range(cols):
            break
        if cave[next_coordinate[0]][next_coordinate[1]] != '.':
            if cave[next_coordinate[0]][next_coordinate[1] - 1] == '.':
                next_coordinate = (next_coordinate[0], next_coordinate[1] - 1)
            elif cave[next_coordinate[0]][next_coordinate[1] + 1] == '.':
                next_coordinate = (next_coordinate[0], next_coordinate[1] + 1)
            else:
                return coordinate
        coordinate = next_coordinate
    return None


f = open("input.txt")
paths = [[tuple(map(int, reversed(coord.split(',')))) for coord in structure.split(" -> ")] for structure in f.read().split('\n')]


rows = [x for structure in paths for x, _ in structure]
cols = [y for structure in paths for _, y in structure]

row_max = max(rows) + 1
col_min = min(cols) - 1

paths1 = [[(x, y - col_min) for x, y in structure] for structure in paths]

start = (0, 500 - col_min)

cols = [y for structure in paths1 for _, y in structure]

col_max = max(cols) + 1


cave  = [['.' for j in range(col_max + 1)]for i in range(row_max)]


for structure in paths1:
    for a, b in zip(structure, structure[1:]):
        for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                cave[i][j] = '#'

cave[start[0]][start[1]]  = '+'
res = simulateSand(start, cave)
counter = 0
while res is not None:
    cave[res[0]][res[1]] = 'o'
    counter += 1
    res = simulateSand(start, cave)

print(f"First solution {counter}")

rows = [x for structure in paths for x, _ in structure]
cols = [y for structure in paths for _, y in structure]

row_max = max(rows) + 2
col_min = min(cols) - 1

paths2 = [[(x, y - col_min) for x, y in structure] for structure in paths]

start = (0, 500 - col_min)

cols = [y for structure in paths2 for _, y in structure]

col_max = max(cols) + 1


cave  = [['.' for j in range(col_max + 1)] for i in range(row_max + 1)]


for structure in paths2:
    for a, b in zip(structure, structure[1:]):
        for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                cave[i][j] = '#'


pad_len = len(cave)
padding = ['.' for i in range(pad_len)]
cave = [padding + row + padding for row in cave]
cave[-1] = ['#' for i in range(len(cave[0]))]

start = (start[0], start[1] + pad_len)
cave[start[0]][start[1]] = '+'

counter = 1
res = simulateSand2(start, cave)
while start != res:
    counter += 1
    cave[res[0]][res[1]] = 'o'
    res = simulateSand2(start, cave)

print(f"Second soultion {counter}")