import heapq
from math import inf

class Solution:
    def getSkyline(self, list_of_buildings):
        list_of_events = []
        for building in list_of_buildings:
            left_edge, right_edge, building_height = building
            # use negative height for start event to simulate max heap
            list_of_events.append((left_edge, -building_height, right_edge))
            list_of_events.append((right_edge, 0, 0))
        list_of_events.sort()

        list_of_key_points = [[0, 0]]
        max_heap = [(0, inf)]  # (negative height, ending x)

        for coordinate_x, negative_height, right_edge in list_of_events:
            # Remove buildings from heap that ended before or at current x
            while max_heap[0][1] <= coordinate_x:
                heapq.heappop(max_heap)

            if negative_height != 0:
                heapq.heappush(max_heap, (negative_height, right_edge))

            current_height = -max_heap[0][0]
            if list_of_key_points[-1][1] != current_height:
                list_of_key_points.append([coordinate_x, current_height])

        if list_of_key_points[0] == [0, 0]:
            list_of_key_points.pop(0)

        return list_of_key_points