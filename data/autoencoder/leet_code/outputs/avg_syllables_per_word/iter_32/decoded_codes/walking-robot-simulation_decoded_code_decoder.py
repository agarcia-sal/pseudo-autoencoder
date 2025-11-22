from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions correspond to: North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        x, y = 0, 0
        dir_index = 0  # initially facing north
        obstacles_set: Set[Tuple[int,int]] = {tuple(ob) for ob in obstacles}
        max_distance = 0

        for command in commands:
            if command == -2:
                dir_index = (dir_index - 1) % 4  # turn left
            elif command == -1:
                dir_index = (dir_index + 1) % 4  # turn right
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x, y = next_x, next_y
                distance = x*x + y*y
                if distance > max_distance:
                    max_distance = distance

        return max_distance