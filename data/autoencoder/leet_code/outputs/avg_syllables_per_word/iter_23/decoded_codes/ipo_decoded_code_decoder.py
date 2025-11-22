import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair each capital with its corresponding profit
        projects = list(zip(capital, profits))
        # Sort projects by required capital ascending
        projects.sort(key=lambda x: x[0])

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Push all projects whose capital requirement <= current w into max_heap
            while i < n and projects[i][0] <= w:
                # Use negative profits to implement max heap in Python
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            # Pop the project with max profit and add to current capital w
            w += -heapq.heappop(max_heap)

        return w