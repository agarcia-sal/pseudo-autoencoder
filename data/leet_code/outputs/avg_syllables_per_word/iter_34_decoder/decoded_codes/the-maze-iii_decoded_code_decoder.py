import heapq
from typing import List, Tuple

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]
        m, n = len(maze), len(maze[0])
        start = (ball[0], ball[1])
        hole = (hole[0], hole[1])
        pq = [(0, "", start)]  # (distance, path, position)
        visited = {}

        while pq:
            dist, path, (x, y) = heapq.heappop(pq)
            if (x, y) == hole:
                return path
            if (x, y) in visited and (visited[(x, y)][0] < dist or (visited[(x, y)][0] == dist and visited[(x, y)][1] <= path)):
                continue
            visited[(x, y)] = (dist, path)

            for dx, dy, d_char in directions:
                new_x, new_y = x, y
                count = 0
                # roll the ball until it hits a wall or hole
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                # only push if this new position offers a better path or hasn't been visited
                if (new_x, new_y) not in visited or dist + count < visited[(new_x, new_y)][0] or (dist + count == visited[(new_x, new_y)][0] and path + d_char < visited[(new_x, new_y)][1]):
                    heapq.heappush(pq, (dist + count, path + d_char, (new_x, new_y)))
        return "impossible"