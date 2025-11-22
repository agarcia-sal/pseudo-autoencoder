import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append([target, 0])

        for position, fuel in stations:
            # Refuel from previous stations with the most fuel first if we can't reach this station
            while max_heap and current_fuel < position:
                refuel_amount = -heapq.heappop(max_heap)
                current_fuel += refuel_amount
                stops += 1
            if current_fuel < position:
                return -1
            heapq.heappush(max_heap, -fuel)

        return stops