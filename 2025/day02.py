#!/usr/bin/env python3
import time
from pathlib import Path
from itertools import combinations

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
    return data.split(',')


def part1(data):
    """
    Solve part 1 using parsed data.
    """
    invalid = 0
    for s in data:
        a, b = s.split("-")
        a = int(a)
        b = int(b)
        for n in range(a, b + 1):
            temp = str(n)
            l = len(temp)
            first = temp[0: l//2]
            second = temp[l//2:]
            if first == second and first[0] != '0' and second[0] != '0':
                # print('IN')
                invalid += int(n)
    return invalid
            
def is_repeated_block(s):
    n = len(s)
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            block = s[:k]
            if block * (n // k) == s:
                return True
    return False

def part2(data):
    """
    Solve part 2 using parsed data.
    """
    invalid = 0
    for s in data:
        a, b = s.split("-")
        a = int(a)
        b = int(b)
        for n in range(a, b + 1):
            temp = str(n)
            if is_repeated_block(temp):
                invalid += int(n)

    return invalid

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
