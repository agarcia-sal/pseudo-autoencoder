from collections import deque
from typing import List, Tuple

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        player_start = None
        box_start = None
        target = None

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    player_start = (i, j)
                elif grid[i][j] == 'B':
                    box_start = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        if player_start is None or box_start is None or target is None:
            return -1

        queue = deque()
        # State: (player_pos, box_pos, push_count)
        queue.append((player_start, box_start, 0))
        visited = set()
        visited.add((player_start, box_start))

        while queue:
            player_pos, box_pos, push_count = queue.popleft()
            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player_x = player_pos[0] + dx
                new_player_y = player_pos[1] + dy
                new_player_pos = (new_player_x, new_player_y)

                if not self.is_valid_position(new_player_pos, grid):
                    continue
                if new_player_pos == box_pos:
                    # Try to push the box
                    new_box_x = box_pos[0] + dx
                    new_box_y = box_pos[1] + dy
                    new_box_pos = (new_box_x, new_box_y)
                    if self.is_valid_position(new_box_pos, grid) and (new_player_pos, new_box_pos) not in visited:
                        visited.add((new_player_pos, new_box_pos))
                        queue.append((new_player_pos, new_box_pos, push_count + 1))
                else:
                    # Move the player without pushing the box
                    if (new_player_pos, box_pos) not in visited:
                        visited.add((new_player_pos, box_pos))
                        queue.append((new_player_pos, box_pos, push_count))

        return -1

    def is_valid_position(self, position: Tuple[int, int], grid: List[List[str]]) -> bool:
        x, y = position
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#':
            return True
        return False