from collections import deque
from typing import List, Tuple, Set

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

        if player_start is None or box_start is None or target is None:
            # If any are missing, impossible scenario
            return -1

        queue = deque()
        queue.append((player_start, box_start, 0))
        visited: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        visited.add((player_start, box_start))

        def is_valid_position(position: Tuple[int, int]) -> bool:
            x, y = position
            return (
                0 <= x < rows and
                0 <= y < cols and
                grid[x][y] != '#'
            )

        while queue:
            player_pos, box_pos, push_count = queue.popleft()

            if box_pos == target:
                return push_count

            for dx, dy in directions:
                new_player_x = player_pos[0] + dx
                new_player_y = player_pos[1] + dy
                new_player_pos = (new_player_x, new_player_y)

                if not is_valid_position(new_player_pos):
                    continue

                if new_player_pos == box_pos:
                    new_box_x = box_pos[0] + dx
                    new_box_y = box_pos[1] + dy
                    new_box_pos = (new_box_x, new_box_y)

                    if (
                        is_valid_position(new_box_pos) and
                        (new_player_pos, new_box_pos) not in visited
                    ):
                        visited.add((new_player_pos, new_box_pos))
                        queue.append((new_player_pos, new_box_pos, push_count + 1))
                else:
                    if (new_player_pos, box_pos) not in visited:
                        visited.add((new_player_pos, box_pos))
                        queue.append((new_player_pos, box_pos, push_count))

        return -1