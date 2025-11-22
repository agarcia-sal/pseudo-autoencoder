from collections import deque
import math

def update_matrix(mat):
    if not mat or not mat[0]:
        return mat
    rows, cols = len(mat), len(mat[0])
    dist = [[math.inf] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist