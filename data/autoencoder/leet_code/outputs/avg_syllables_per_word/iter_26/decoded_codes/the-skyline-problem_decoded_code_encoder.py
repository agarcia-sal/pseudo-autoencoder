import heapq
import math
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left_edge, right_edge, building_height in buildings:
            # start of building has negative height for max-heap simulation
            events.append((left_edge, -building_height, right_edge))
            # end of building has 0 height
            events.append((right_edge, 0, 0))

        events.sort()

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negative_height, right_bound)

        for position_x, negative_height, right_bound in events:
            # Remove the buildings from heap which ended before or at position_x
            while max_heap and max_heap[0][1] <= position_x:
                heapq.heappop(max_heap)

            if negative_height != 0:
                heapq.heappush(max_heap, (negative_height, right_bound))

            # If current max height differs from last recorded height in result, record new key point
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([position_x, current_height])

        # Remove the initial dummy point if still present
        if result[0] == [0, 0]:
            result.pop(0)

        return result