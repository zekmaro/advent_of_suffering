def read_data(filename):
	with open(filename, 'r') as f:
		data = []
		for line in f.readlines():
			data.append(line.strip())
	return data

def part1(data):
	vowels = {"a", "e", "i", "o", "u"}
	forbidden = {"ab", "cd", "pq", "xy"}

	counter = 0

	for s in data:
		vowel_count = 0
		has_double = False
		has_forbidden = False

		for i in range(len(s)):
			ch = s[i]

			if ch in vowels:
				vowel_count += 1

			if i > 0:
				prev = s[i-1]

				if ch == prev:
					has_double = True

				if prev + ch in forbidden:
					has_forbidden = True
					break

		if vowel_count >= 3 and has_double and not has_forbidden:
			counter += 1

	return counter


def part2(data):
	pass


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))