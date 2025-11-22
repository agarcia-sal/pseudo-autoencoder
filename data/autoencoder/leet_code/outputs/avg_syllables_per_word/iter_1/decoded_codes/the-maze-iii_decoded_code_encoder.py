from heapq import heappush, heappop

def find_path(maze, ball, hole):
    dirs = [(0,1,'r'), (1,0,'d'), (0,-1,'l'), (-1,0,'u')]
    m, n = len(maze), len(maze[0])
    start, hole = tuple(ball), tuple(hole)
    pq = [(0, "", start)]
    visited = set()

    while pq:
        dist, path, (x, y) = heappop(pq)
        if (x, y) == hole:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy, d in dirs:
            nx, ny, cnt = x, y, 0
            while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                cnt += 1
                if (nx, ny) == hole:
                    break
            if (nx, ny) not in visited:
                heappush(pq, (dist + cnt, path + d, (nx, ny)))

    return "impossible"