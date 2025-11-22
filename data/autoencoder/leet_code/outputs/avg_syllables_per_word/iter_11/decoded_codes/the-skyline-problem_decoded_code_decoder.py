from heapq import heappush, heappop
from math import inf

class Solution:
    def getSkyline(self, buildings):
        events = []
        for building in buildings:
            left, right, height = building
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort(key=lambda x: (x[0], x[1], x[2]))
        result = [[0, 0]]
        max_heap = [(0, inf)]
        for x, negH, r in events:
            while max_heap[0][1] <= x:
                heappop(max_heap)
            if negH != 0:
                heappush(max_heap, (negH, r))
            if result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])
        if result[0] == [0, 0]:
            result.pop(0)
        return result