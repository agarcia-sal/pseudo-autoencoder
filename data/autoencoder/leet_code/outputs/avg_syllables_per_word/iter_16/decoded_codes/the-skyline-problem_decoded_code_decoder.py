import heapq
import math

class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        result = [[0, 0]]
        max_heap = [(0, math.inf)]  # (negative height, right)

        for x, neg_h, r in events:
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if neg_h != 0:
                heapq.heappush(max_heap, (neg_h, r))
            current_height = -max_heap[0][0]
            if result[-1][1] != current_height:
                result.append([x, current_height])

        if result[0] == [0, 0]:
            result.pop(0)
        return result