from collections import deque
from typing import List, Tuple, Set

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        player_start = None
        box_start = None
        target = None

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                c = grid[i][j]
                if c == 'S':  # player start
                    player_start = (i, j)
                elif c == 'B':  # box start
                    box_start = (i, j)
                elif c == 'T':  # target
                    target = (i, j)

        if player_start is None or box_start is None or target is None:
            return -1  # invalid input, missing required positions

        visited: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        queue = deque()
        queue.append((player_start, box_start, 0))
        visited.add((player_start, box_start))

        while queue:
            player_pos, box_pos, push_count = queue.popleft()

            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player_x = player_pos[0] + dx
                new_player_y = player_pos[1] + dy
                new_player_pos = (new_player_x, new_player_y)

                if self.is_valid_position(new_player_pos, grid):
                    if new_player_pos == box_pos:
                        new_box_x = box_pos[0] + dx
                        new_box_y = box_pos[1] + dy
                        new_box_pos = (new_box_x, new_box_y)
                        if self.is_valid_position(new_box_pos, grid) and (new_player_pos, new_box_pos) not in visited:
                            visited.add((new_player_pos, new_box_pos))
                            queue.append((new_player_pos, new_box_pos, push_count + 1))
                    else:
                        if (new_player_pos, box_pos) not in visited:
                            visited.add((new_player_pos, box_pos))
                            queue.append((new_player_pos, box_pos, push_count))

        return -1

    def is_valid_position(self, position: Tuple[int, int], grid: List[List[str]]) -> bool:
        x, y = position
        rows, cols = len(grid), len(grid[0])
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#':
            return True
        return False