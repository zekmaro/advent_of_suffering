instructions = {}

def read_data(filename):
	with open(filename, 'r') as f:
		for line in f:
			parts = line.strip().split()
			
			tup = None
			if len(parts) == 3:
				if parts[0].isdigit():
					tup = ("VALUE", parts[0])
				else:
					tup = ("WIRE", parts[0])

			elif len(parts) == 4:
				tup = ("NOT", parts[1])

			elif len(parts) == 5:
				tup = (parts[1], parts[0], parts[2])
			
			instructions[parts[-1]] = tup

	return instructions

cache = {}

def solve(wire):
	if wire.isdigit():
		return int(wire)

	if wire in cache:
		return cache[wire]

	op = instructions[wire]
	match op[0]:
		case "VALUE":
			result = int(op[1])
		case "WIRE":
			result = solve(op[1])
		case "NOT":
			result = ~solve(op[1]) & 0xFFFF
		case "AND":
			result = solve(op[1]) & solve(op[2])
		case "OR":
			result = solve(op[1]) | solve(op[2])
		case "LSHIFT":
			result = (int(solve(op[1])) << int(op[2])) & 0xFFFF
		case "RSHIFT":
			result = (int(solve(op[1])) >> int(op[2])) & 0xFFFF

	cache[wire] = result
	return result

def part1():
	for op in instructions:
		solve(op[-1])
	return cache['a']

def part2():
	pass


if __name__ == "__main__":
	filename = 'input.txt'
	read_data(filename)
	print(part1())
	print(part2())
