import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: x[0])

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                # Use negative profits to simulate max heap with heapq
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w