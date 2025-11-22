def read_data(filename):
	with open(filename, 'r') as f:
		instractions = []
		for line in f:
			parts = line.strip().split()
			if parts[0] == "toggle":
				cmd = "toggle"
				coord1 = parts[1]
				coord2 = parts[3]
			else:
				# parts[0] == "turn", parts[1] is "on" or "off"
				cmd = f"{parts[0]} {parts[1]}"
				coord1 = parts[2]
				coord2 = parts[4]
			
			x1, y1 = map(int, coord1.split(','))
			x2, y2 = map(int, coord2.split(','))

			instractions.append((cmd, x1, y1, x2, y2))

	return instractions


def part1(data):
	grid = [[0] * 1000 for _ in range(1000)]
	for instr in data:
		for x in range(instr[1], instr[3] + 1):
			for y in range(instr[2], instr[4] + 1):
				if instr[0] == 'toggle':
					grid[x][y] ^= 1
				elif instr[0] == 'turn off':
					grid[x][y] = 0
				elif instr[0] == 'turn on':
					grid[x][y] = 1
	
	counter = sum(light for row in grid for light in row)
	
	return counter


def part2(data):
	grid = [[0] * 1000 for _ in range(1000)]
	for instr in data:
		for x in range(instr[1], instr[3] + 1):
			for y in range(instr[2], instr[4] + 1):
				if instr[0] == 'toggle':
					grid[x][y] += 2
				elif instr[0] == 'turn off':
					grid[x][y] = max(0, grid[x][y] - 1)
				elif instr[0] == 'turn on':
					grid[x][y] += 1
	
	counter = sum(light for row in grid for light in row)
	
	return counter


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))
