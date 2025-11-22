import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, height, right in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        # Sort by x position, then by height (negH), then by right
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negH, right)

        for x, negH, r in events:
            # Remove buildings from heap that ended before or exactly at x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            # If it's a start of building, add to heap
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # If current max height changes, append to result
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])

        # Remove the initial dummy if still present
        if result[0] == [0, 0]:
            result.pop(0)

        return result