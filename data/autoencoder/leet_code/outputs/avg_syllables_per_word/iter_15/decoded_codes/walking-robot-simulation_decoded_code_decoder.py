from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x: int = 0
        y: int = 0
        dir_index: int = 0
        obstacles_set: Set[Tuple[int, int]] = set(map(tuple, obstacles))
        max_distance: int = 0

        for command in commands:
            if command == -2:
                dir_index = (dir_index - 1) % 4
            elif command == -1:
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                squared_distance = x * x + y * y
                if squared_distance > max_distance:
                    max_distance = squared_distance

        return max_distance