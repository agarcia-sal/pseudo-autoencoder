import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: x[0])

        max_heap = []
        i, n = 0, len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w