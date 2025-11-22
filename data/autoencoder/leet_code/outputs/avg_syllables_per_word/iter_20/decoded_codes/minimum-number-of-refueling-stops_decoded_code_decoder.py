import heapq
from typing import List, Tuple

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[Tuple[int, int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        # Append the target with zero fuel so we treat it as a station to reach
        stations.append((target, 0))

        for position, fuel in stations:
            while max_heap and current_fuel < position:
                largest_fuel_to_add = -heapq.heappop(max_heap)
                current_fuel += largest_fuel_to_add
                stops += 1
            if current_fuel < position:
                return -1
            heapq.heappush(max_heap, -fuel)

        return stops