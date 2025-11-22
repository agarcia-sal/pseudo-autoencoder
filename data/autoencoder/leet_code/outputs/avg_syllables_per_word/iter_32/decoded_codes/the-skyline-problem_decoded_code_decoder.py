import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        # Create two events per building: entering (left) and leaving (right)
        # entering event: (x, -height, right)
        # leaving event: (x, 0, 0)
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        # Sort events by x, then by height, then by right
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        # Result initialized with a base ground line [0,0]
        result = [[0, 0]]
        # max_heap will hold (-height, right)
        max_heap = [(0, float('inf'))]  # ground height with infinite right boundary

        for x, negH, r in events:
            # Remove buildings from heap that have ended before or at x
            while max_heap and max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            # If this is a start of building (negH != 0), add it to heap
            if negH != 0:
                heapq.heappush(max_heap, (negH, r))

            current_height = -max_heap[0][0]  # max height now
            last_height = result[-1][1]
            if last_height != current_height:
                result.append([x, current_height])

        # Remove the initial [0,0] if still present
        if result and result[0] == [0, 0]:
            result.pop(0)

        return result