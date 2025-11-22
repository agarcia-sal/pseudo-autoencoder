class Solution:
    def robotSim(self, commands, obstacles):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # North, East, South, West
        x = y = 0
        direction_index = 0  # initially facing north
        obstacles_set = set(map(tuple, obstacles))
        max_dist = 0

        for command in commands:
            if command == -2:
                direction_index = (direction_index - 1) % 4
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles_set:
                        break
                    x, y = nx, ny
                dist = x*x + y*y
                if dist > max_dist:
                    max_dist = dist

        return max_dist