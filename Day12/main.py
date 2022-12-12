from decimal import Decimal

class VertexData:
    def __init__(self, neighbours, distance, previous):
        self.neighbours = neighbours
        self.distance = distance
        self.previous = previous
    def append(self, item):
        self.neighbours.append(item)

def minDist(graph, unvisited_nodes):
    min = Decimal('Infinity')
    idxMin = None
    for idx in unvisited_nodes:
        if graph[idx].distance < min:
            min = graph[idx].distance
            idxMin = idx
    return idxMin


f = open("input.txt")
grid = [list(row) for row in f.read().split('\n')]

start = (0, 0)
end = (0, 0)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            grid[i][j] = 'a'
        if grid[i][j] == 'E':
            end = (i, j)
            grid[i][j] = 'z'


graph = {(i, j): VertexData([], Decimal('Infinity'), None) for i in range(len(grid)) for j in range(len(grid[0]))}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i - 1 >= 0 and ord(grid[i - 1][j]) - ord(grid[i][j]) <= 1:
            graph[(i, j)].append((i - 1, j))
        if j - 1 >= 0 and ord(grid[i][j - 1]) - ord(grid[i][j]) <= 1:
            graph[(i, j)].append((i, j - 1))
        if i + 1 < len(grid) and ord(grid[i + 1][j]) - ord(grid[i][j]) <= 1:
            graph[(i, j)].append((i + 1, j))
        if j + 1 < len(grid[0]) and ord(grid[i][j + 1]) - ord(grid[i][j]) <= 1:
            graph[(i, j)].append((i, j + 1))


curr_idx = start
graph[start].distance = 0
unvisited_nodes = list(graph.keys())

while True:
    curr_idx = minDist(graph, unvisited_nodes)
    unvisited_nodes.remove(curr_idx)
    if curr_idx == end:
        break
    curr_dist = graph[curr_idx].distance
    for idx in graph[curr_idx].neighbours:
        if graph[idx].distance > curr_dist + 1:
            graph[idx].distance = curr_dist + 1
            graph[idx].previous = curr_idx

    
print(f"First solution {graph[end].distance}")

graph = {(i, j): VertexData([], Decimal('Infinity'), None) for i in range(len(grid)) for j in range(len(grid[0]))}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i - 1 >= 0 and ord(grid[i - 1][j]) - ord(grid[i][j]) >= -1:
            graph[(i, j)].append((i - 1, j))
        if j - 1 >= 0 and ord(grid[i][j - 1]) - ord(grid[i][j]) >= -1:
            graph[(i, j)].append((i, j - 1))
        if i + 1 < len(grid) and ord(grid[i + 1][j]) - ord(grid[i][j]) >= -1:
            graph[(i, j)].append((i + 1, j))
        if j + 1 < len(grid[0]) and ord(grid[i][j + 1]) - ord(grid[i][j]) >= -1:
            graph[(i, j)].append((i, j + 1))


curr_idx = end
graph[end].distance = 0
unvisited_nodes = list(graph.keys())

while True:
    curr_idx = minDist(graph, unvisited_nodes)
    i, j = curr_idx
    if grid[i][j] == 'a':
        break
    unvisited_nodes.remove(curr_idx)
    curr_dist = graph[curr_idx].distance
    for idx in graph[curr_idx].neighbours:
        if graph[idx].distance > curr_dist + 1:
            graph[idx].distance = curr_dist + 1
            graph[idx].previous = curr_idx

print(f"Second solution {graph[curr_idx].distance}")






        
        

