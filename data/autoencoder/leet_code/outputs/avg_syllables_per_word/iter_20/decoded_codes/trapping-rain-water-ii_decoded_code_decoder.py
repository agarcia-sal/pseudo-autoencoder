import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        for i in range(m):
            # Left border
            heapq.heappush(min_heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            # Right border
            heapq.heappush(min_heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][n - 1] = True

        for j in range(n):
            # Top border
            heapq.heappush(min_heap, (heightMap[0][j], 0, j))
            visited[0][j] = True
            # Bottom border
            heapq.heappush(min_heap, (heightMap[m - 1][j], m - 1, j))
            visited[m - 1][j] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water_trapped = 0

        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    trapped = max(0, height - heightMap[nx][ny])
                    water_trapped += trapped
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))

        return water_trapped