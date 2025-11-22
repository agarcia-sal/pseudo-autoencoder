import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            if i == n - 1 and j == n - 1:
                return t

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    new_time = max(t, grid[ni][nj])
                    heapq.heappush(min_heap, (new_time, ni, nj))

        return -1