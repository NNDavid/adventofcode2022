from functools import cmp_to_key

def compare(fst, snd):
    if isinstance(fst, int) and isinstance(snd, int):
        return 0 if fst == snd else (-1 if fst < snd else 1)
    elif isinstance(fst, int) and not isinstance(snd, int):
        return compare(list([fst]), snd)
    elif not isinstance(fst, int) and isinstance(snd, int):
        return compare(fst, list([snd]))
    else:
        for f, s in zip(fst, snd):
            result = compare(f, s)
            if result == 0:
                continue
            return result
        return 0 if len(fst) == len(snd) else (-1 if  len(fst) < len(snd) else 1)

f = open("input.txt")
pairs = [tuple([eval(item) for item in pair.split('\n')]) for pair in f.read().split('\n\n')]

print(f"First solution {sum([i + 1 for i in range(len(pairs)) if compare(pairs[i][0], pairs[i][1]) == -1])}")

add_1 = [[2]]
add_2 = [[6]]
packets = [add_1, add_2] + [fst for fst, _ in pairs] + [snd for _, snd in pairs]
packets.sort(key = cmp_to_key(compare))

print(f"Second solution {(packets.index(add_1) + 1) * (packets.index(add_2) + 1)}")