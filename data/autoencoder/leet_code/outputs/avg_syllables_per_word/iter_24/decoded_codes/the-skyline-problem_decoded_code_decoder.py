import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            left, right, height = building
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort(key=lambda x: (x[0], x[1]))

        result = [[0, 0]]
        max_heap = [(0, float('inf'))]  # (negative_height, right_edge)

        for x, neg_height, right_edge in events:
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, right_edge))
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)
        return result