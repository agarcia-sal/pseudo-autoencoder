from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        x = y = 0
        dir_index = 0
        obstacles_set: Set[Tuple[int, int]] = set(map(lambda obs: (obs[0], obs[1]), obstacles))
        max_distance = 0

        for command in commands:
            if command == -2:  # turn left
                dir_index = (dir_index - 1) % 4
            elif command == -1:  # turn right
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                max_distance = max(max_distance, x*x + y*y)

        return max_distance