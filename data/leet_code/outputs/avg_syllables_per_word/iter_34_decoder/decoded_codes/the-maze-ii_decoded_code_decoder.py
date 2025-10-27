from heapq import heappush, heappop

class Solution:
    def shortestDistance(self, maze, start, destination):
        m = len(maze)
        n = len(maze[0]) if m > 0 else 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        start = tuple(start)
        destination = tuple(destination)
        visited = set()
        pq = [(0, start)]  # (distance, position)

        while pq:
            dist, position = heappop(pq)
            x, y = position

            if position == destination:
                return dist
            if position in visited:
                continue
            visited.add(position)

            for dx, dy in directions:
                new_x, new_y = x, y
                count = 0
                # roll until hit wall or boundary
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                if (new_x, new_y) not in visited:
                    heappush(pq, (dist + count, (new_x, new_y)))

        return -1