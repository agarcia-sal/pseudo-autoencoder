import heapq
from typing import List, Tuple

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions: List[Tuple[int, int, str]] = [
            (0, 1, 'r'),  # right
            (1, 0, 'd'),  # down
            (0, -1, 'l'), # left
            (-1, 0, 'u')  # up
        ]

        m, n = len(maze), len(maze[0])
        start = tuple(ball)
        hole = tuple(hole)

        # Priority queue: (distance, path, (x,y))
        pq = [(0, '', start)]
        visited = set()

        while pq:
            dist, path, (x, y) = heapq.heappop(pq)
            if (x, y) == hole:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy, d in directions:
                new_x, new_y = x, y
                count = 0
                # Move until hitting wall or hole
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, path + d, (new_x, new_y)))

        return "impossible"