import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            # Start event has negative height to differentiate from end event
            events.append((left, -height, right))
            # End event has height 0, indicating building ends
            events.append((right, 0, 0))
        events.sort()

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (neg_height, right)

        for x, negH, r in events:
            # Remove buildings from heap which ended before current x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            # If it's a start event, add building height to heap
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # Current max height is -max_heap[0][0]
            current_height = -max_heap[0][0]
            # If height changed from last point, append new point to result
            if result[-1][1] != current_height:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)
        return result