import heapq
from typing import List, Tuple

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[Tuple[int, int]]) -> int:
        max_heap = []  # max heap implemented as a min heap with negated values
        current_fuel = startFuel
        stops = 0

        # Append (target, 0) as the destination with no fuel
        stations.append((target, 0))

        for position, fuel in stations:
            # Refuel from past stops until we have enough fuel to reach this station
            while max_heap and current_fuel < position:
                removed_fuel = -heapq.heappop(max_heap)
                current_fuel += removed_fuel
                stops += 1

            if current_fuel < position:
                return -1

            # We add current station's fuel as negative to implement max heap
            heapq.heappush(max_heap, -fuel)

        return stops