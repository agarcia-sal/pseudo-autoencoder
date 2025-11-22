import heapq
from typing import List, Tuple

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions: List[Tuple[int, int]] = [(1,0), (-1,0), (0,1), (0,-1)]
        start_t = tuple(start)
        destination_t = tuple(destination)
        visited = set()
        pq = [(0, start_t)]  # (distance, (x,y))

        while pq:
            dist, (x, y) = heapq.heappop(pq)
            if (x, y) == destination_t:
                return dist
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x, y
                count = 0
                # roll the ball until hitting a wall or boundary
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, (new_x, new_y)))

        return -1