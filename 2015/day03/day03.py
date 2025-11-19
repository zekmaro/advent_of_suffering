def read_data(filename):
	with open(filename, 'r') as f:
		data = f.read().strip()

	return data

def part1(data):
	houses_count = 1
	x, y = 0, 0
	cur_coor = (x, y)
	visited = [cur_coor]
	for dir in data:

		if dir == '>':
			x += 1
		elif dir == '<':
			x -= 1
		elif dir == 'v':
			y -= 1
		elif dir == '^':
			y += 1

		cur_coor = (x, y)

		if cur_coor not in visited:
			visited.append(cur_coor)
			houses_count += 1
	
	return houses_count

def part2(data):
	# Movement mapping: direction -> (dx, dy)
	moves = {
		'>': (1, 0),
		'<': (-1, 0),
		'^': (0, 1),
		'v': (0, -1)
	}

	# Santa = index 0, Robot = index 1
	positions = [(0, 0), (0, 0)]

	visited = {(0, 0)}   # use a set
	houses = 1

	for i, step in enumerate(data):
		who = i % 2  # 0 = santa, 1 = robot

		dx, dy = moves[step]
		x, y = positions[who]

		x += dx
		y += dy
		positions[who] = (x, y)

		if (x, y) not in visited:
			visited.add((x, y))
			houses += 1

	return houses


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))