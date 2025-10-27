import heapq

class Solution:
    def findShortestWay(self, maze, ball, hole):
        directions = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]
        m, n = len(maze), len(maze[0])
        hole = tuple(hole)
        start = tuple(ball)

        pq = [(0, "", start)]
        visited = set()

        while pq:
            dist, path, (x, y) = heapq.heappop(pq)
            if (x, y) == hole:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy, dch in directions:
                new_x, new_y = x, y
                count = 0
                # Roll the ball until it hits a wall or the hole
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, path + dch, (new_x, new_y)))

        return "impossible"