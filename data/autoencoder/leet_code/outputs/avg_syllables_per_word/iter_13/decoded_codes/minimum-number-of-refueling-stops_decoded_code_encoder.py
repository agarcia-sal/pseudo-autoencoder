import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append([target, 0])

        for position, fuel in stations:
            # Refuel from past stations if not enough fuel to reach the current station
            while max_heap and current_fuel < position:
                largest_fuel = -heapq.heappop(max_heap)  # Get the station with the largest fuel
                current_fuel += largest_fuel
                stops += 1
            if current_fuel < position:
                return -1
            heapq.heappush(max_heap, -fuel)

        return stops