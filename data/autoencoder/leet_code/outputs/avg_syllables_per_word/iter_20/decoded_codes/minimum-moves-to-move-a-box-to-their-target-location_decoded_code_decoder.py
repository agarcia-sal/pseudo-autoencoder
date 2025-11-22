from collections import deque
from typing import List, Tuple

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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

        if not (player_start and box_start and target):
            return -1  # missing required elements

        visited = set()
        queue = deque()
        queue.append((player_start, box_start, 0))
        visited.add((player_start, box_start))

        while queue:
            player_pos, box_pos, push_count = queue.popleft()
            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player_pos = (player_pos[0] + dx, player_pos[1] + dy)
                if not self.is_valid_position(new_player_pos, grid):
                    continue

                if new_player_pos == box_pos:
                    new_box_pos = (box_pos[0] + dx, box_pos[1] + dy)
                    if (self.is_valid_position(new_box_pos, grid) and 
                        (new_player_pos, new_box_pos) not in visited):
                        visited.add((new_player_pos, new_box_pos))
                        queue.append((new_player_pos, new_box_pos, push_count + 1))
                else:
                    if (new_player_pos, box_pos) not in visited:
                        visited.add((new_player_pos, box_pos))
                        queue.append((new_player_pos, box_pos, push_count))

        return -1

    def is_valid_position(self, position: Tuple[int, int], grid: List[List[str]]) -> bool:
        x, y = position
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'