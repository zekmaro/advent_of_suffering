from collections import deque

def bfs(start, is_goal, neighbors):
    """Generic BFS."""
    dq = deque([start])
    seen = {start}
    while dq:
        cur = dq.popleft()
        if is_goal(cur):
            return cur
        for nx in neighbors(cur):
            if nx not in seen:
                seen.add(nx)
                dq.append(nx)
