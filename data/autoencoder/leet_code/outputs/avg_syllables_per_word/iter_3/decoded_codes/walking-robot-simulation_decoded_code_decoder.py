from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        dir_index = 0
        obstacles_set = set(map(tuple, obstacles))
        max_distance = 0

        for command in commands:
            if command == -2:
                dir_index = (dir_index - 1) % 4
            elif command == -1:
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                max_distance = max(max_distance, x*x + y*y)

        return max_distance