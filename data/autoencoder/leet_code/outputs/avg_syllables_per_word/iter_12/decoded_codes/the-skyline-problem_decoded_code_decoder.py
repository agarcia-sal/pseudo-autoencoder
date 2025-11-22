import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            left, right, height = building
            events.append((left, -height, right))  # start of building
            events.append((right, 0, 0))           # end of building
        events.sort()

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (neg_height, right)

        for x, negH, r in events:
            # Remove buildings from heap that ended before or at x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)
        return result