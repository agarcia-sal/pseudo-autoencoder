import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append([target, 0])

        for position, fuel in stations:
            while max_heap and current_fuel < position:
                # Pop the largest fuel from heap (stored as negative)
                current_fuel += -heapq.heappop(max_heap)
                stops += 1

            if current_fuel < position:
                return -1

            # Push current station's fuel as negative for max heap behavior
            heapq.heappush(max_heap, -fuel)

        return stops