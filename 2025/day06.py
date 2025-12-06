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
    ops = [c for c in lines[-1] if c in "+-*"]
    nums = [
        [int(x) for x in line.split()]
        for line in lines[:-1]
    ]
    raw_num_lines = lines[:-1]
    ops_line = lines[-1]

    return nums, raw_num_lines, ops_line


def part1(nums, ops):
    """
    Solve part 1 using parsed data.
    """
    rows = len(nums)
    cols = len(nums[0])
    res = 0
    for j in range(cols):
        op = ops[j]
        if op == '*':
            val = 1
        else:
            val = 0
        for i in range(rows):
            if op == '*':
                val *= nums[i][j]
            elif op == '+':
                val += nums[i][j]
        res += val
    return res


def part2(raw_lines, ops_line):
    rows = len(raw_lines)

    width = max(len(ops_line), *(len(line) for line in raw_lines))
    grid = [line.ljust(width) for line in raw_lines]
    ops_line = ops_line.ljust(width)

    ops = [(i, c) for i, c in enumerate(ops_line) if c in "+*"]
    ops.reverse()

    res = 0
    for pos, op in ops:
        L = pos
        while L > 0:
            if all(grid[r][L-1] == ' ' for r in range(rows)):
                break
            L -= 1

        R = pos
        while R + 1 < width:
            if all(grid[r][R+1] == ' ' for r in range(rows)):
                break
            R += 1

        nums = []
        for c in range(R, L - 1, -1):
            digits = [grid[r][c] for r in range(rows)]
            s = "".join(digits).strip()
            nums.append(int(s))

        if op == '+':
            val = sum(nums)
        else:
            val = 1
            for n in nums:
                val *= n

        res += val

    return res


# ---- RUNNER ----------------------------------------------------------------

def run():
    data_raw = read_input()
    nums, raw_lines, ops_line = parse(data_raw)

    # t0 = time.time()
    # p1 = part1(nums, ops)
    t1 = time.time()
    p2 = part2(raw_lines, ops_line)
    t2 = time.time()

    print(f"Day {DAY[-2:]}:")
    # print(f"  Part 1: {p1}  ({(t1 - t0)*1000:.3f} ms)")
    print(f"  Part 2: {p2}  ({(t2 - t1)*1000:.3f} ms)")


if __name__ == "__main__":
    run()
