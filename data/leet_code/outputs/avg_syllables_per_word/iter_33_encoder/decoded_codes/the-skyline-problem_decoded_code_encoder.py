import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            left, right, height = building
            # Add start event with negative height for max-heap simulation
            events.append((left, -height, right))
            # Add end event
            events.append((right, 0, 0))

        # Sort by x position, then height, then right position
        events.sort(key=lambda e: (e[0], e[1], e[2]))

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negHeight, endPos)

        for x, negH, r in events:
            # Remove ended buildings from heap
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            # If it's a start event, add building to heap
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # If current max height changed, record the skyline point
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)

        return result