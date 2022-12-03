import string

value_dict = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))

f = open('input.txt', mode = 'r')
rucksacks = f.read().split('\n')

result1 = 0
for rucksack in rucksacks:
	length = len(rucksack) // 2
	first = set(rucksack[:length])
	second = set(rucksack[length:])
	common_items = first.intersection(second)
	for item in common_items:
		result1 += value_dict[item]

print(f"First solution: {result1}")

result2 = 0
for i in range(len(rucksacks) // 3):
	common = set((rucksacks[i * 3]))
	for j in range(1,3):
		common = common.intersection(set((rucksacks[i * 3 + j])))
	for item in common:
		result2 += value_dict[item]

print(f"Second solution: {result2}")