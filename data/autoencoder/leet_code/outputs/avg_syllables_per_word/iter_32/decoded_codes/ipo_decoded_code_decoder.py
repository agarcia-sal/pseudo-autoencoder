from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair up capital and profits, then sort by capital requirement
        projects = sorted(zip(capital, profits), key=lambda x: x[0])

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Add all projects that can be started with current capital w to the max_heap
            while i < n and projects[i][0] <= w:
                # Python has min heap, so push negative profit to simulate max heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                # No projects can be started at this capital level
                break

            # Pop the project with the maximum profit and add its profit to capital w
            w += -heapq.heappop(max_heap)

        return w