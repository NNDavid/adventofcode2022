def start_of_packet(input, length):
    for i in range(len(input)-length):
        if len(set(input[i:i+length])) == length:
            return i + length

f = open("input.txt")
input = f.read()

print(f"First solution {start_of_packet(input, 4)}")
print(f"Second solution {start_of_packet(input, 14)}")