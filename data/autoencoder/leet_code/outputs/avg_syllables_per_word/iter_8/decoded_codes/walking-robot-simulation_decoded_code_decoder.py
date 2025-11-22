class Solution:
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = 0
        y = 0
        dir_index = 0
        obstacles_set = set((ox, oy) for ox, oy in obstacles)
        max_distance = 0

        for command in commands:
            if command == -2:
                dir_index -= 1
                if dir_index < 0:
                    dir_index += 4
            elif command == -1:
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacles_set:
                        break
                    x = next_x
                    y = next_y
                current_distance = x * x + y * y
                if current_distance > max_distance:
                    max_distance = current_distance

        return max_distance