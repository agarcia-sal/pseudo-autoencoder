import heapq
import math

def get_skyline(buildings):
    # Create events list
    events = []
    for b in buildings:
        events.append((b.left, -b.height, b.right))
        events.append((b.right, 0, 0))
    events.sort()

    res = [[0, 0]]
    # Use a heap of (-height, end) intervals
    heap = [(0, math.inf)]

    for x, h, r in events:
        # Remove ended buildings from heap
        while heap[0][1] <= x:
            heapq.heappop(heap)
        # If this is a building start, add it to heap
        if h != 0:
            heapq.heappush(heap, (h, r))
        # If current max height has changed, add the point to result
        if res[-1][1] != -heap[0][0]:
            res.append([x, -heap[0][0]])

    if res[0] == [0, 0]:
        res.pop(0)
    return res