from typing import List, Tuple
import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions: List[Tuple[int, int, str]] = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]
        m, n = len(maze), len(maze[0])
        start = (ball[0], ball[1])
        hole_pos = (hole[0], hole[1])
        pq: List[Tuple[int, str, Tuple[int, int]]] = [(0, '', start)]
        visited = set()

        while pq:
            dist, path, (x, y) = heapq.heappop(pq)

            if (x, y) == hole_pos:
                return path

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy, direction in directions:
                new_x, new_y = x, y
                count = 0

                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole_pos:
                        break

                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, path + direction, (new_x, new_y)))

        return "impossible"