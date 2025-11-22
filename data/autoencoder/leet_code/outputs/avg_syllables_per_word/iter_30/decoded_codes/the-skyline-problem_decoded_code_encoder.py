import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            # Building start event has negative height to prioritize higher buildings
            events.append((left, -height, right))
            # Building end event
            events.append((right, 0, 0))
        events.sort()

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negHeight, right)

        for x, negH, r in events:
            # Remove all buildings from heap that ended before or at x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                # Push new building into the heap
                heapq.heappush(max_heap, (negH, r))
            # Current max height is -max_heap[0][0]
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])
        if result[0] == [0, 0]:
            result.pop(0)
        return result