import heapq
from typing import List, Tuple

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        number_of_rows = len(maze)
        number_of_columns = len(maze[0]) if maze else 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        visited = set()
        priority_queue = [(0, start)]  # heapq with (distance, (x, y))

        while priority_queue:
            dist, (x, y) = heapq.heappop(priority_queue)

            if (x, y) == destination:
                return dist

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x, y
                count = 0

                # Roll the ball until it hits a wall or edge
                while 0 <= new_x + dx < number_of_rows and 0 <= new_y + dy < number_of_columns and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1

                if (new_x, new_y) not in visited:
                    heapq.heappush(priority_queue, (dist + count, (new_x, new_y)))

        return -1