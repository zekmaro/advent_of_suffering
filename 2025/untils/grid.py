DIRS4 = [(1,0), (-1,0), (0,1), (0,-1)]
DIRS8 = [(1,0), (-1,0), (0,1), (0,-1), (1,1),(1,-1),(-1,1),(-1,-1)]

def neighbors4(x,y):
    for dx,dy in DIRS4:
        yield x+dx, y+dy

def neighbors8(x,y):
    for dx,dy in DIRS8:
        yield x+dx, y+dy
