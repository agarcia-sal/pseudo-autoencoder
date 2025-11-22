from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        dir_index = 0
        obstacles_set = self.convert_obstacles_to_set(obstacles)
        max_distance = 0

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
                current_distance = x * x + y * y
                if current_distance > max_distance:
                    max_distance = current_distance

        return max_distance

    def convert_obstacles_to_set(self, obstacles: List[List[int]]) -> set:
        return {tuple(obstacle) for obstacle in obstacles}