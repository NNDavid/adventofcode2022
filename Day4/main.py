def contains(sector1, sector2):
	return sector1[0] >= sector2[0] and sector1[1] <= sector2[1]

def overlaps(sector1, sector2):
	return (sector1[0] >= sector2[0] and sector1[0] <= sector2[1]) or (sector1[1] >= sector2[0] and sector1[1] <= sector2[1])


f = open('input.txt', mode = 'r')

pairs = f.read().split('\n')

counter = 0
for pair in pairs:
	elves = pair.split(',')
	sector1 = [int(sector) for sector in elves[0].split('-')]
	sector2 = [int(sector) for sector in elves[1].split('-')]
	if contains(sector1, sector2) or contains(sector2, sector1):
		counter +=1

print(f"First solution {counter}")

counter = 0
for pair in pairs:
	elves = pair.split(',')
	sector1 = [int(sector) for sector in elves[0].split('-')]
	sector2 = [int(sector) for sector in elves[1].split('-')]
	if overlaps(sector1, sector2) or overlaps(sector2, sector1):
		counter +=1

print(f"Second solution {counter}")
