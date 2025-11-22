import heapq
import math

class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()

        result = [[0, 0]]
        max_heap = [(0, math.inf)]

        for x, negH, r in events:
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            if result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])

        if result[0] == [0, 0]:
            result.pop(0)
        return result