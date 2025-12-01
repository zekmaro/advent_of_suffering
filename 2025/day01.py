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
    return data.splitlines()


def part1(data):
    pos = 50
    count = 0

    for rot in data:
        dir = rot[0]
        num = int(rot[1:])

        if dir == 'R':
            pos += num
        else:
            pos -= num

        pos %= 100
        if pos == 0:
            count += 1

    return count


def part2(data):
    pos = 50
    count = 0

    for rot in data:
        dir = rot[0]
        num = int(rot[1:])

        for _ in range(num):
            if dir == 'R':
                pos = (pos + 1) % 100
            else:
                pos = (pos - 1) % 100

            if pos == 0:
                count += 1

    return(count)

# ---- RUNNER ----------------------------------------------------------------

def run():
    data_raw = read_input()
    data = parse(data_raw)

    t0 = time.time()
    p1 = part1(data)
    t1 = time.time()
    p2 = part2(data)
    t2 = time.time()

    print(f"Day {DAY[-2:]}:")
    print(f"  Part 1: {p1}  ({(t1 - t0)*1000:.3f} ms)")
    print(f"  Part 2: {p2}  ({(t2 - t1)*1000:.3f} ms)")


if __name__ == "__main__":
    run()
