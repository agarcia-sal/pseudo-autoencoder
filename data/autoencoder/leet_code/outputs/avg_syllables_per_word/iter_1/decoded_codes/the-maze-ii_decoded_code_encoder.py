import heapq

def shortestDistance(maze, start, destination):
    m, n = len(maze), len(maze[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    start, dest = tuple(start), tuple(destination)
    visited = set()
    pq = [(0, start)]

    while pq:
        dist, (x, y) = heapq.heappop(pq)
        if (x, y) == dest:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in dirs:
            nx, ny, step = x, y, 0
            while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                step += 1
            if (nx, ny) not in visited:
                heapq.heappush(pq, (dist + step, (nx, ny)))

    return -1