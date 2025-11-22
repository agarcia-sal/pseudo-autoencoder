import heapq
from typing import List, Tuple

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = self.initialize_visited(m, n)
        min_heap = []

        for i in range(m):
            self.push_to_heap(min_heap, heightMap[i][0], i, 0)
            self.push_to_heap(min_heap, heightMap[i][n - 1], i, n - 1)
            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(n):
            self.push_to_heap(min_heap, heightMap[0][j], 0, j)
            self.push_to_heap(min_heap, heightMap[m - 1][j], m - 1, j)
            visited[0][j] = True
            visited[m - 1][j] = True

        directions = self.define_directions()
        water_trapped = 0

        while min_heap:
            height, x, y = self.pop_from_heap(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    water_trapped += max(0, height - heightMap[nx][ny])
                    self.push_to_heap(min_heap, max(height, heightMap[nx][ny]), nx, ny)

        return water_trapped

    def initialize_visited(self, m: int, n: int) -> List[List[bool]]:
        return [[False] * n for _ in range(m)]

    def push_to_heap(self, heap: List[Tuple[int, int, int]], height: int, x: int, y: int) -> None:
        heapq.heappush(heap, (height, x, y))

    def pop_from_heap(self, heap: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        return heapq.heappop(heap)

    def define_directions(self) -> List[Tuple[int, int]]:
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]