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
	counter = 0
	for s in data:
		doubles_cond = False
		triples_cond = False
		pairs = {}
		for i in range(len(s)):

			if i >= 2 and s[i] == s[i - 2]:
				triples_cond = True

			if i >= 1:
				pair = s[i-1:i+1]
				if pair not in pairs:
					pairs[pair] = []
				pairs[pair].append(i - 1)

		# not effitient loop
		for positions in pairs.values():
			for i in range(len(positions)):
				for j in range(i + 1, len(positions)):
					if positions[j] - positions[i] >= 2:
						doubles_cond = True
						break

		if doubles_cond and triples_cond:
			counter += 1

	return counter


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))