def read_data(filename):
	with open(filename, 'r') as f:
		data = f.read().strip()

	return data

def part1(data):
	res = 0
	for i in range(len(data)):
		if data[i] == '(':
			res += 1
		else:
			res -= 1
	return res

def part2(data):
	res = 0
	for i in range(len(data)):
		if data[i] == '(':
			res += 1
		else:
			res -= 1

		if res == -1:
			return i + 1
	return -1

if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))