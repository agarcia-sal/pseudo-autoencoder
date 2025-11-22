from collections import deque

class Solution:
    def minPushBox(self, grid):
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        player_start = box_start = target = None

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                c = grid[i][j]
                if c == 'S':
                    player_start = (i, j)
                elif c == 'B':
                    box_start = (i, j)
                elif c == 'T':
                    target = (i, j)

        queue = deque([(player_start, box_start, 0)])
        visited = set()
        visited.add((player_start, box_start))

        def is_valid_position(pos):
            x, y = pos
            return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'

        while queue:
            player_pos, box_pos, push_count = queue.popleft()
            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player_pos = (player_pos[0] + dx, player_pos[1] + dy)
                if not is_valid_position(new_player_pos):
                    continue

                if new_player_pos == box_pos:
                    new_box_pos = (box_pos[0] + dx, box_pos[1] + dy)
                    if is_valid_position(new_box_pos) and (new_player_pos, new_box_pos) not in visited:
                        visited.add((new_player_pos, new_box_pos))
                        queue.append((new_player_pos, new_box_pos, push_count + 1))
                else:
                    if (new_player_pos, box_pos) not in visited:
                        visited.add((new_player_pos, box_pos))
                        queue.append((new_player_pos, box_pos, push_count))

        return -1