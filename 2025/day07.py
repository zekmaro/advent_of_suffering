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

def find_next_splitter(grid, r, c, cache_next_splitter):
    if (r, c) in cache_next_splitter:
        return cache_next_splitter[(r, c)]

    rows = len(grid)
    while r < rows and grid[r][c] != '^':
        r += 1

    if r >= rows:
        cache_next_splitter[(r, c)] = None
    else:
        cache_next_splitter[(r, c)] = r

    return cache_next_splitter[(r, c)]

def dfs(grid, i, j, cache_next_splitter, cache_paths_count):
    rows = len(grid)
    cols = len(grid[0])

    if j < 0 or j >= cols or i >= rows:
        return 1

    if (i, j) in cache_paths_count:
        return cache_paths_count[(i, j)]

    next_splitter = find_next_splitter(grid, i, j, cache_next_splitter)

    if next_splitter is None:
        cache_paths_count[(i, j)] = 1
        return 1

    left = dfs(grid, next_splitter + 1, j - 1, cache_next_splitter, cache_paths_count)
    right = dfs(grid, next_splitter + 1, j + 1, cache_next_splitter, cache_paths_count)

    cache_paths_count[(i, j)] = left + right
    return cache_paths_count[(i, j)]


def shoot(grid, i, j, visited_beams, visited_splitters, splits):
    rows = len(grid)
    cols = len(grid[0])

    if (i, j) in visited_beams:
        return
    visited_beams.add((i, j))

    if j < 0 or j >= cols or i >= rows:
        return

    while i < rows and grid[i][j] != '^':
        i += 1
    
    if i >= rows:
        return

    if (i, j) not in visited_splitters:
        visited_splitters.add((i, j))
        splits[0] += 1

    shoot(grid, i + 1, j - 1, visited_beams, visited_splitters, splits)
    shoot(grid, i + 1, j + 1, visited_beams, visited_splitters, splits)


def find_s_pos(grid):
    for r, row in enumerate(grid):
        if "S" in row:
            col = row.index("S")
            row = r
            break
    return row, col

def part1(grid):
    """
    Solve part 1 using parsed data.
    """
    visited_beams = set()
    visited_splitters = set()
    splits = [0]
    row, col = find_s_pos(grid)
    
    shoot(grid, row + 1, col, visited_beams, visited_splitters, splits)
    return splits[0]


def part2(grid):
    """
    Solve part 2 using parsed data.
    """
    cache_next_splitter = {}
    cache_paths_count = {}
    row, col = find_s_pos(grid)

    res = dfs(grid, row + 1, col, cache_next_splitter, cache_paths_count)
    return res

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
