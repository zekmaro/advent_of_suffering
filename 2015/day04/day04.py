import hashlib


def read_data(filename):
	with open(filename, 'r') as f:
		data = f.read().strip()

	return data


def part1(data):
	i = 0
	while True:
		i += 1
		hasher = hashlib.md5()
		encoded_data = (data + str(i)).encode()
		hasher.update(encoded_data)
		digest = hasher.hexdigest()
		if digest[:5] == "00000":
			break

	return i


def part2(data):
	i = 0
	while True:
		i += 1
		hasher = hashlib.md5()
		encoded_data = (data + str(i)).encode()
		hasher.update(encoded_data)
		digest = hasher.hexdigest()
		if digest[:6] == "000000":
			break

	return i


if __name__ == "__main__":
	filename = 'input.txt'
	data = read_data(filename)
	print(part1(data))
	print(part2(data))
