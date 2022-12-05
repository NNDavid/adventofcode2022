
f = open('input.txt', mode = 'r')

line = f.readline()

row = [line[i * 4 + 1] for i in range(len(line) // 4)]
crates = [[] for i in range(len(row))]

while row[0].isalpha() or row[0] == ' ':
	crates =[crates[i] +[row[i]] if row[i] != ' ' else [] for i in range(len(crates))]
	line = f.readline()
	row = [line[i * 4 + 1] for i in range(len(line) // 4)]

crates2 = crates.copy()
f.readline()
commands = [line.split(' ') for line in f]
for command in commands:
	quantity = int(command[1])
	source = int(command[3]) - 1
	target = int(command[5]) - 1
	to_move = crates[source][:quantity]
	crates[source] = crates[source][quantity:]
	to_move.reverse()
	crates[target] = to_move + crates[target]

print(f"First solution: {''.join([crate[0] for crate in crates])}")

for command in commands:
	quantity = int(command[1])
	source = int(command[3]) - 1
	target = int(command[5]) - 1
	to_move = crates2[source][:quantity]
	crates2[source] = crates2[source][quantity:]
	crates2[target] = to_move + crates2[target]s

print(f"Second solution: {''.join([crate[0] for crate in crates2])}")