from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        x = y = 0
        dir_index = 0
        obstacles_set: Set[Tuple[int, int]] = set((ox, oy) for ox, oy in obstacles)
        max_distance = 0

        for command in commands:
            if command == -2:  # turn left
                dir_index = (dir_index - 1) % 4
            elif command == -1:  # turn right
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                dist = x*x + y*y
                if dist > max_distance:
                    max_distance = dist

        return max_distance