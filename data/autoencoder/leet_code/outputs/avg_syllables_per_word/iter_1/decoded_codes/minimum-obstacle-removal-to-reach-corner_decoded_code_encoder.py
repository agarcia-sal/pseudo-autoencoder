import heapq

def minimum_cost_path(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    heap = [(0, 0, 0)]  # cost, x, y
    visited = {(0, 0)}

    while heap:
        cost, x, y = heapq.heappop(heap)
        if (x, y) == (m-1, n-1):
            return cost
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(heap, (cost + grid[nx][ny], nx, ny))

    return -1