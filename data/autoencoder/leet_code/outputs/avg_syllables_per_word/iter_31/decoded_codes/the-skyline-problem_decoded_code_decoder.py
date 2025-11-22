import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            left, right, height = building
            # Start event has negative height to ensure correct max-heap behavior
            events.append((left, -height, right))
            # End event
            events.append((right, 0, 0))

        # Sort events by x, then by height, then by right
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        # Result starts with dummy ground height
        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (neg_height, right), initial ground with infinite right

        for x, negH, r in events:
            # Remove buildings that ended before or at current x
            while max_heap and max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            if negH != 0:
                # Add new building
                heapq.heappush(max_heap, (negH, r))

            current_height = -max_heap[0][0]
            last_height = result[-1][1]
            if last_height != current_height:
                result.append([x, current_height])

        # Remove initial dummy if still present
        if result[0] == [0, 0]:
            result.pop(0)

        return result