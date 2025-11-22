import heapq
from math import inf
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            # Left edge: height is negative to distinguish start of building
            events.append((left, -height, right))
            # Right edge: zero height to indicate end of building
            events.append((right, 0, 0))
        # Sort by x, then height, then right
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        result = [[0, 0]]
        max_heap = [(0, inf)]  # (neg_height, right)

        for x, negH, r in events:
            # Remove buildings from heap that ended before x
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