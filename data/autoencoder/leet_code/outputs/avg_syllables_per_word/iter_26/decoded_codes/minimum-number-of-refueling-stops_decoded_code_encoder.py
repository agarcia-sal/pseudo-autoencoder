import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append([target, 0])

        for position, fuel in stations:
            # Refuel from the largest available fuel stops until we can reach current station
            while max_heap and current_fuel < position:
                largest_fuel = -heapq.heappop(max_heap)
                current_fuel += largest_fuel
                stops += 1

            if current_fuel < position:
                return -1

            # Add current station's fuel to max_heap
            heapq.heappush(max_heap, -fuel)

        return stops