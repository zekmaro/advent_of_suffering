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

dirs = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

def part1(grid):
    """
    Solve part 1 using parsed data.
    """
    ans = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                count = 0
                for i, j in dirs:
                    temp_r = r + i
                    temp_c = c + j

                    if temp_r >= 0 and temp_r < rows and temp_c >= 0 and temp_c < cols:
                        if grid[temp_r][temp_c] == '@':
                            count += 1
                
                if count < 4:
                    ans += 1
                
    return ans

from collections import deque

def part2(grid):
    """
    Solve part 2 using parsed data.
    """
    grid = [list(row) for row in grid]
    q = deque()
    ans = 0
    rows = len(grid)
    cols = len(grid[0])
    neighbor_count = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                count = 0
                for i, j in dirs:
                    temp_r = r + i
                    temp_c = c + j

                    if temp_r >= 0 and temp_r < rows and temp_c >= 0 and temp_c < cols:
                        if grid[temp_r][temp_c] == '@':
                            count += 1
                            neighbor_count[r][c] += 1
                
                if count < 4:
                    q.append((r, c))

    removed = set()
    while q:
        r, c = q.popleft()
        if (r, c) in removed:
            continue
        removed.add((r, c))
        grid[r][c] = '.'
        ans += 1
        for i, j in dirs:
            temp_r = r + i
            temp_c = c + j

            if temp_r >= 0 and temp_r < rows and temp_c >= 0 and temp_c < cols:
                if grid[temp_r][temp_c] == '@':
                    neighbor_count[temp_r][temp_c] -= 1
                    if neighbor_count[temp_r][temp_c] < 4:
                        q.append((temp_r, temp_c))

    return ans

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
