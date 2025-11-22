import heapq
from typing import List, Tuple

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[Tuple[int, int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append((target, 0))

        prev_position = 0
        for position, fuel in stations:
            distance = position - prev_position

            while max_heap and current_fuel < distance:
                # Pop the largest fuel from max_heap (stored as negative values)
                largest_fuel_available = -heapq.heappop(max_heap)
                current_fuel += largest_fuel_available
                stops += 1

            if current_fuel < distance:
                return -1

            current_fuel -= distance
            prev_position = position
            heapq.heappush(max_heap, -fuel)

        return stops