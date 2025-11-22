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
        number_of_rows = len(maze)
        number_of_columns = len(maze[0]) if maze else 0
        start_position = (ball[0], ball[1])
        hole_position = (hole[0], hole[1])
        priority_queue = [(0, '', start_position)]
        visited_positions = set()

        while priority_queue:
            current_distance, path, current_position = heapq.heappop(priority_queue)
            current_x, current_y = current_position

            if current_position == hole_position:
                return path

            if current_position in visited_positions:
                continue
            visited_positions.add(current_position)

            for dx, dy, direction_char in directions:
                new_x, new_y = current_x, current_y
                roll_count = 0

                # Roll the ball until it hits a wall or falls into the hole
                while 0 <= new_x + dx < number_of_rows and 0 <= new_y + dy < number_of_columns and \
                      maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    roll_count += 1
                    if (new_x, new_y) == hole_position:
                        break

                if (new_x, new_y) not in visited_positions:
                    heapq.heappush(priority_queue, (current_distance + roll_count, path + direction_char, (new_x, new_y)))

        return "impossible"