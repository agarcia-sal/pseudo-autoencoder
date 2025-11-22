from heapq import heappop, heappush
from typing import List, Tuple

class Solution:
    def findShortestWay(
        self,
        maze: List[List[int]],
        ball: List[int],
        hole: List[int]
    ) -> str:
        directions: List[Tuple[int, int, str]] = [
            (0, 1, 'r'),
            (1, 0, 'd'),
            (0, -1, 'l'),
            (-1, 0, 'u')
        ]
        m, n = len(maze), len(maze[0]) if maze else 0
        start = tuple(ball)
        hole = tuple(hole)
        pq = [(0, "", start)]
        visited = set()

        while pq:
            dist, path, (x, y) = heappop(pq)
            if (x, y) == hole:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy, dchar in directions:
                new_x, new_y = x, y
                count = 0
                while (
                    0 <= new_x + dx < m and
                    0 <= new_y + dy < n and
                    maze[new_x + dx][new_y + dy] == 0
                ):
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                if (new_x, new_y) not in visited:
                    heappush(pq, (dist + count, path + dchar, (new_x, new_y)))
        return "impossible"