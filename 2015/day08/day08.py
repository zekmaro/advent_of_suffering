def read_data(filename):
	with open(filename, 'r') as f:
		data = []
		for line in f.readlines():
			data.append(line.strip())
	return data


def part1(data):
	pass


def part2(data):
    pass


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))
