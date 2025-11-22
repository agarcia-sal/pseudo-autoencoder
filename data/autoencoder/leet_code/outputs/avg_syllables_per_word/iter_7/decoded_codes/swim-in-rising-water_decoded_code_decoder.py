import heapq
from typing import List, Set, Tuple

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited: Set[Tuple[int, int]] = {(0, 0)}
        min_heap: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            if i == n - 1 and j == n - 1:
                return t
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heapq.heappush(min_heap, (max(t, grid[ni][nj]), ni, nj))
        return -1