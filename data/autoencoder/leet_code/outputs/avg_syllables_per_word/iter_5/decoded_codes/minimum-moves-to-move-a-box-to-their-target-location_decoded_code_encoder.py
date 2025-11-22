from collections import deque

class Solution:
    def minPushBox(self, grid):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        m, n = len(grid), len(grid[0])
        player_start = box_start = target = None

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player_start = (i, j)
                elif grid[i][j] == 'B':
                    box_start = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        def is_valid_position(pos):
            x, y = pos
            return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

        queue = deque([(player_start, box_start, 0)])
        visited = {(player_start, box_start)}

        while queue:
            player_pos, box_pos, push_count = queue.popleft()
            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player = (player_pos[0] + dx, player_pos[1] + dy)
                if not is_valid_position(new_player):
                    continue

                if new_player == box_pos:
                    new_box = (box_pos[0] + dx, box_pos[1] + dy)
                    if is_valid_position(new_box) and (new_player, new_box) not in visited:
                        visited.add((new_player, new_box))
                        queue.append((new_player, new_box, push_count + 1))
                else:
                    if (new_player, box_pos) not in visited:
                        visited.add((new_player, box_pos))
                        queue.append((new_player, box_pos, push_count))

        return -1