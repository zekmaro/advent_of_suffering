def read_data(filename):
	with open(filename, 'r') as f:
		data = []
		for line in f.readlines():
			data.append(line.strip().split('x'))
	return data


def part1(data):
	total = 0
	for line in data:
		l, w, h = map(int, line)

		# areas of the 3 sides
		a1 = l * w
		a2 = w * h
		a3 = h * l

		# surface area
		surface = 2*a1 + 2*a2 + 2*a3

		# slack: smallest side area
		slack = min(a1, a2, a3)

		total += surface + slack

	return total


def part2(data):
    total = 0
    for line in data:
        l, w, h = map(int, line)

        # sort original dimensions (not areas!)
        x, y, z = sorted([l, w, h])

        # smallest perimeter
        ribbon_wrap = 2*x + 2*y

        # bow = volume
        bow = l * w * h

        total += ribbon_wrap + bow

    return total



if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))
