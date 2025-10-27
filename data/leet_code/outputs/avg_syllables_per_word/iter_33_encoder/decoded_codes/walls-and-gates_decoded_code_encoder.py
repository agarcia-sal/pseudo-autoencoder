from collections import deque
from typing import List, Optional

class Solution:
    def wallsAndGates(self, rooms: Optional[List[List[int]]]) -> None:
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Initialize queue with all gates' positions (rooms[r][c] == 0)
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2147483647

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))