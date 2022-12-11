def perform_op(r_l, op):
    for i in range(len(r_l)):
        r_l[i] = eval(op, {"old": r_l[i]}) % divisible[i]


#PART 1
f = open("input.txt")
monkeys = f.read().split('\n\n')

handled = [0 for i in range(len(monkeys))]
items = []
operation = []
divisible = []
throw = []

for monkey in monkeys:
    rows = monkey.split('\n')
    items.append(list(map(int, rows[1][18:].split(', '))))
    operation.append(rows[2][19:])
    divisible.append(int(rows[3][21:]))
    throw.append((int(rows[4][29:]), int(rows[5][30:])))

for rounds in range(20):
    for i in range(len(monkeys)):
        handled[i] += len(items[i])
        for j in range(len(items[i])):
            items[i][j] = eval(operation[i], {"old": items[i][j]}) // 3
            if items[i][j] % divisible[i] == 0:
                items[throw[i][0]].append(items[i][j])
            else:
                items[throw[i][1]].append(items[i][j])
        items[i] = []

handled.sort()

print(f"First solution {handled[-1] * handled[-2]}")

#PART 2
handled = [0 for i in range(len(monkeys))]
items = []
operation = []
divisible = []
throw = []

rem_list = []

for monkey in monkeys:
    rows = monkey.split('\n')
    items.append(list(map(int, rows[1][18:].split(', '))))
    operation.append(rows[2][19:])
    divisible.append(int(rows[3][21:]))
    throw.append((int(rows[4][29:]), int(rows[5][30:])))

for monkey_list in items:
    div_list = []
    for item in monkey_list:
        div_list.append([item % div for div in divisible])
    rem_list.append(div_list)
    

for rounds in range(10000):
    print(rounds)
    for i in range(len(monkeys)):
        handled[i] += len(rem_list[i])
        for j in range(len(rem_list[i])):
            perform_op(rem_list[i][j], operation[i])
            if rem_list[i][j][i] == 0:
                rem_list[throw[i][0]].append(rem_list[i][j])
            else:
                rem_list[throw[i][1]].append(rem_list[i][j])
        rem_list[i] = []


handled.sort()

print(f"Second soluion {handled[-1] * handled[-2]}")