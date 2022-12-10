f = open("input.txt")
rows = f.read().split('\n')

cycle = 1
X = 1
values = []

for row in rows:
    if row == "noop":
        values.append((cycle, X))
        cycle += 1
    else:
        values.append((cycle, X))
        values.append((cycle + 1, X))
        _, a = row.split(' ')
        X += int(a)
        cycle += 2
print(sum([val * c for c, val in values  if c in [20, 60, 100, 140, 180, 220]]))


screen = [['.' for j in range (40)]for i in range(6)]


for i in range(6):
    for j in range(40):
        cycle = i * 40 + j
        if values[cycle][1] in range(j - 1, j + 2):
            screen[i][j] = '#'

for pixels in screen:
    print("".join(pixels))