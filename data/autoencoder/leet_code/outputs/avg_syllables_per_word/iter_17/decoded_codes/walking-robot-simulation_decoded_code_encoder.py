class Solution:
    def robotSim(self, commands, obstacles):
        directions = self.DirectionsList()
        x, y = 0, 0
        dir_index = 0
        obstacles_set = self.ConvertListOfListsToSet(obstacles)
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
                max_distance = max(max_distance, x * x + y * y)
        return max_distance

    def DirectionsList(self):
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def ConvertListOfListsToSet(self, list_of_lists):
        return set((x, y) for x, y in list_of_lists)