def calc_size(dir_name):
    stack = [dir_name]
    subdirs_added = {dir : False for dir in size_dict.keys()}
    while len(stack) > 0:
        curr_dir = stack[-1]
        dir_list = dir_dict[curr_dir]
        if len(dir_list) > 0 and not subdirs_added[curr_dir]:
            stack = stack + dir_list
            subdirs_added[curr_dir] = True
        else:
            size_dict[curr_dir] += sum([size_dict[dir] for dir in dir_list])
            stack.pop()

def getName(dirL):
    name = dirL[0]
    for dirName in dirL[1:]:
        name += '/' + dirName
    return name




f = open("input.txt")
commands = f.read().split('\n')

dir_stack = []
current_dir = ""

dir_dict = dict()
size_dict = dict()

for command in commands:
    parts = command.split(' ')
    if parts[0] == '$':
        if parts[1] == "cd":
            if parts[2] == "..":
                dir_stack.pop()
            else:
                dir_stack.append(parts[2])
            current_dir = getName(dir_stack)
            if current_dir not in dir_dict.keys():
                dir_dict[current_dir] = []
                size_dict[current_dir] = 0
    else:
        if parts[0] == "dir":
            dir_dict[current_dir].append(current_dir + '/' + parts[1])
        else:
            size_dict[current_dir] += int(parts[0])

calc_size('/')

print(f"First solution: {sum([size[1] for size in size_dict.items() if size[1] <= 100000])}")

needed = 30000000 - (70000000 - size_dict['/'])

print(f"Second solution: {min([size[1] for size in size_dict.items() if size[1] - needed >= 0])}")