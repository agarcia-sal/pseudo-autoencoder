import heapq
from typing import List, Tuple

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start = (start[0], start[1])
        destination = (destination[0], destination[1])

        visited = set()
        pq = [(0, start)]  # (distance, (x, y))

        while pq:
            dist, position = heapq.heappop(pq)
            x, y = position

            if position == destination:
                return dist

            if position in visited:
                continue

            visited.add(position)

            for dx, dy in directions:
                new_x, new_y = x, y
                count = 0

                # Roll the ball until it hits a wall or boundary
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1

                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, (new_x, new_y)))

        return -1