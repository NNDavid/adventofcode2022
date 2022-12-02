f = open('input.txt', mode = 'r')
elves = f.read()
elf_calory = [sum([int(calory) for calory in elf.split('\n')]) for elf in elves.split('\n\n')]
# Puzzle 1
print(f"Part 1: {max(elf_calory)}")

# Puzzle 2
elf_calory.sort()
print(f"Part 2: {sum(elf_calory[-3:])}")