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
    """
    Solve part 1 using parsed data.
    """
    total = 0
    for line in data:
        best = -1
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                d1 = int(line[i])
                d2 = int(line[j])
                pair = d1 * 10 + d2
                best = max(best, pair)

        total += best
    return total


def part2(data):
    """
    Solve part 2 using parsed data.
    """
    total = 0
    for line in data:
        stack = []
        n = len(line)
        k = 12
        out = n - k
        for i in range(n):
            while stack and stack[-1] < line[i] and out > 0:
                stack.pop()
                out -= 1

            stack.append(line[i])
        
        while out > 0:
            stack.pop()
            out -= 1

        num = 0
        for d in stack:
            num = num * 10 + int(d)
        
        total += num
        
    return total

# ---- RUNNER ----------------------------------------------------------------

def run():
    data_raw = read_input()
    data = parse(data_raw)

    # t0 = time.time()
    # p1 = part1(data)
    t1 = time.time()
    p2 = part2(data)
    t2 = time.time()

    print(f"Day {DAY[-2:]}:")
    # print(f"  Part 1: {p1}  ({(t1 - t0)*1000:.3f} ms)")
    print(f"  Part 2: {p2}  ({(t2 - t1)*1000:.3f} ms)")


if __name__ == "__main__":
    run()
