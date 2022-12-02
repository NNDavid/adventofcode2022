f = open('input.txt', mode = 'r')

content = f.read()

scores = {('A', 'Y') : 6, ('A', 'Z') : 0, ('B', 'X') : 0, ('B', 'Z') : 6, ('C', 'X') : 6, ('C', 'Y') : 0, ('A', 'X') : 3, ('B', 'Y') : 3, ('C', 'Z') : 3}
playPoint = {'X' : 1, 'Y' : 2, 'Z' : 3}

games = [game.split(' ') for game in content.split('\n')]

result1 = sum([scores[(game[0], game[1])] + playPoint[game[1]] for game in games])
print(f"Part 1: {result1}")

strategy={'X' : 0, 'Y' : 3, 'Z' : 6}
toPlay = {('A', 'X') : 'Z', ('A', 'Y') : 'X', ('A', 'Z') : 'Y', ('B', 'X') : 'X', ('B', 'Y') : 'Y', ('B', 'Z') : 'Z', ('C', 'X') : 'Y', ('C', 'Y') : 'Z', ('C', 'Z') : 'X'}


result2 = sum([strategy[game[1]] + playPoint[toPlay[(game[0], game[1])]] for game in games])
print(f"Part 2: {result2}")







