import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            left, right, height = building
            events.append((left, -height, right))
            events.append((right, 0, 0))
        # Sort events by x, then height, then right
        events.sort(key=lambda e: (e[0], e[1], e[2]))

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negative_height, right)
        for x, negH, r in events:
            # Remove buildings from heap that ended before or at current x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            # If this is a start of building, add it
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # If current max height changed, add to result
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])
        # Remove initial dummy if still present
        if result and result[0] == [0, 0]:
            result.pop(0)
        return result