from collections import deque

def min_flips(mat):
    m, n = len(mat), len(mat[0])
    target = tuple([0] * n for _ in range(m))
    start = tuple(tuple(row) for row in mat)
    queue = deque([(start, 0)])
    visited = {start}

    def neighbors(i, j):
        for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                yield x, y

    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps
        matrix = [list(row) for row in state]

        for i in range(m):
            for j in range(n):
                nxt = [r[:] for r in matrix]
                for x, y in neighbors(i, j):
                    nxt[x][y] ^= 1
                nxt_state = tuple(tuple(row) for row in nxt)
                if nxt_state not in visited:
                    visited.add(nxt_state)
                    queue.append((nxt_state, steps + 1))

    return -1