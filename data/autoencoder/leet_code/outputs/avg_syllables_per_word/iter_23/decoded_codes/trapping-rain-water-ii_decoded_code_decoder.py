import heapq
from typing import List, Optional

class Solution:
    def trapRainWater(self, heightMap: Optional[List[List[int]]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        # Push all boundary cells onto the heap and mark them visited
        for i in range(m):
            heapq.heappush(min_heap, (heightMap[i][0], i, 0))
            heapq.heappush(min_heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(n):
            heapq.heappush(min_heap, (heightMap[0][j], 0, j))
            heapq.heappush(min_heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water_trapped = 0

        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    neighbor_height = heightMap[nx][ny]
                    # If current boundary is higher, water can be trapped
                    if height > neighbor_height:
                        water_trapped += height - neighbor_height
                    # Push the max height boundary
                    heapq.heappush(min_heap, (max(height, neighbor_height), nx, ny))

        return water_trapped