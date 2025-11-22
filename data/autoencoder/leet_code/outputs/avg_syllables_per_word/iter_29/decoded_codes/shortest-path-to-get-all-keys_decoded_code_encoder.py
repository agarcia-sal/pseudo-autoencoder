from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        start_position = None
        number_of_keys = 0

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                current_cell = grid[i][j]
                if current_cell == '@':
                    start_position = (i, j)
                elif 'a' <= current_cell <= 'z':
                    number_of_keys += 1

        queue = deque([(start_position[0], start_position[1], 0, 0)])  # x, y, keys bitmask, steps
        visited_states = set([(start_position[0], start_position[1], 0)])

        all_keys_bitmask = (1 << number_of_keys) - 1

        while queue:
            x, y, collected_keys, steps = queue.popleft()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < number_of_rows and 0 <= new_y < number_of_columns:
                    next_cell = grid[new_x][new_y]

                    if next_cell == '#':
                        continue

                    if 'A' <= next_cell <= 'Z':
                        required_key_bitmask = 1 << (ord(next_cell.lower()) - ord('a'))
                        if (collected_keys & required_key_bitmask) == 0:
                            continue

                    if 'a' <= next_cell <= 'z':
                        new_collected_keys = collected_keys | (1 << (ord(next_cell) - ord('a')))
                        if new_collected_keys == all_keys_bitmask:
                            return steps + 1
                    else:
                        new_collected_keys = collected_keys

                    state = (new_x, new_y, new_collected_keys)
                    if state not in visited_states:
                        visited_states.add(state)
                        queue.append((new_x, new_y, new_collected_keys, steps + 1))

        return -1