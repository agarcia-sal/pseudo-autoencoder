from typing import List, Tuple
import heapq
import math

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events: List[Tuple[int, int, int]] = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort(key=lambda x: (x[0], x[1]))

        result: List[List[int]] = [[0, 0]]
        max_heap: List[Tuple[int, int]] = [(0, math.inf)]  # (neg_height, right)

        for x, negH, r in events:
            # Remove buildings from the heap where right <= x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            current_height = -max_heap[0][0]
            if current_height != result[-1][1]:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)
        return result