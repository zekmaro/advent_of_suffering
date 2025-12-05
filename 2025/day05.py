#!/usr/bin/env python3
import time
from pathlib import Path

DAY = Path(__file__).stem  # "day01"

# ---- INPUT LOADING ----------------------------------------------------------

def read_input(example=False):
    fname = f"inputs/{DAY}{'_example' if example else ''}.txt"
    return Path(fname).read_text().strip()

# ---- SOLUTION ---------------------------------------------------------------

def parse(data):
    """
    Convert the raw input into a useful structure.
    Example:
        return [int(x) for x in data.splitlines()]
    """
    lines = data.splitlines()
    data = [line.strip() for line in lines]
    sep_idx = data.index("")
    p1 = data[:sep_idx]
    p2 = data[sep_idx + 1:]
    ranges = []
    for line in p1:
        a, b = line.split("-")
        ranges.append((int(a), int(b)))
    ranges = sorted(ranges, key= lambda x: x[0])
    merged = []
    current_start, current_end = ranges[0]
    for a, b in ranges[1:]:
        if a <= current_end:
            current_end = max(current_end, b)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = a, b
    merged.append((current_start, current_end))

    numbers = [int(x) for x in p2]
    numbers = sorted(numbers)
    return merged, numbers


def part1(ranges, numbers):
    """
    Solve part 1 using parsed data.
    """
    i = 0
    j = 0
    res = 0
    while i < len(ranges) and j < len(numbers):
        a, b = ranges[i]
        num = numbers[j]

        if num < a:
            j += 1
        elif num > b:
            i += 1
        else:
            res += 1
            j += 1

    return res


def part2(ranges):
    """
    Solve part 2 using parsed data.
    """
    res = 0
    for a, b in ranges:
        res += (b - a + 1)

    return res

# ---- RUNNER ----------------------------------------------------------------

def run():
    data_raw = read_input()
    ranges, numbers = parse(data_raw)

    t0 = time.time()
    p1 = part1(ranges, numbers)
    t1 = time.time()
    p2 = part2(ranges)
    t2 = time.time()

    print(f"Day {DAY[-2:]}:")
    print(f"  Part 1: {p1}  ({(t1 - t0)*1000:.3f} ms)")
    print(f"  Part 2: {p2}  ({(t2 - t1)*1000:.3f} ms)")


if __name__ == "__main__":
    run()
