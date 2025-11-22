import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        start, destination = tuple(start), tuple(destination)
        visited = set()
        pq = [(0, start)]

        while pq:
            dist, (x, y) = heapq.heappop(pq)
            if (x, y) == destination:
                return dist
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x, y
                count = 0
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, (new_x, new_y)))
        return -1