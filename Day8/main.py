f = open("input.txt")
rows = f.read().split('\n')

grid = [[int(num) for num in row] for row in rows]

counter = 2 * (len(grid) + len(grid[0]) - 2)

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        height = grid[i][j]
        left = [value < height for value in grid[i][:j]]
        right = [value < height for value in grid[i][j + 1:]]
        
        top = [value[j] < height for value in grid[:i]]
        bottom = [value[j] < height for value in grid[i + 1:]]

        if all(left) or all(right) or all(top) or all(bottom):
            counter += 1

print(f"First solution {counter}")

scores = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        height = grid[i][j]
        left = 0
        right = 0
        top = 0
        bottom = 0
        for k in reversed(range(0, i)):
            top += 1
            if grid[k][j] >= height:
                break

        for k in range(i + 1, len(grid)):
            bottom += 1
            if grid[k][j] >= height:
                break
        
        for k in reversed(range(0, j)):
            left += 1
            if grid[i][k] >= height:
                break

        for k in range(j + 1, len(grid[0])):
            right += 1
            if grid[i][k] >= height:
                break
        scores.append(left * right * top * bottom)
        print(f"{i} {j} top = {top} bottom = {bottom} left = {left} right = {right}")

print(scores)

print(f"Second solution {max(scores)}")
