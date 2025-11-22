import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            # Left edge event: use negative height for max heap and to differentiate start from end
            events.append((left, -height, right))
            # Right edge event: height zero to indicate end of building
            events.append((right, 0, 0))
        # Sort events:
        # First by position, then by height so that start edges (-height) come before end edges (0)
        events.sort(key=lambda x: (x[0], x[1]))

        result = [[0,0]]
        max_heap = [(0, math.inf)]  # (neg_height, end_position)

        for x, negH, r in events:
            # Remove buildings from heap which have ended before or at this point x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # Current highest building height
            current_height = -max_heap[0][0]
            # If current height differs from last recorded height, add to result
            if result[-1][1] != current_height:
                result.append([x, current_height])
        # Remove the initial dummy result if it remains
        if result[0] == [0, 0]:
            result.pop(0)
        return result