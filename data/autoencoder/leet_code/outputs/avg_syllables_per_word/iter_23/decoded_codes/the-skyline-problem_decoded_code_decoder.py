import heapq
import math

class Solution:
    def getSkyline(self, buildings):
        # Create list of all events: (x, neg_height, right)
        events = []
        for left, height, right in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        # Sort events by x, then by height, then by right
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        result = [[0, 0]]
        # max_heap stores tuples of (-height, right)
        max_heap = [(0, math.inf)]

        for x, negH, r in events:
            # Remove all buildings from heap where right <= x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))
            # Current max height is -max_heap[0][0]
            if result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])

        # Remove initial [0,0] if still present
        if result[0] == [0, 0]:
            result.pop(0)
        return result