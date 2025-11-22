import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        # Append the target as a station with 0 fuel to simplify calculation
        stations.append([target, 0])
        max_heap = []
        current_fuel = startFuel
        stops = 0

        for position, fuel in stations:
            # Refuel with the largest fuel tank(s) passed so far until we can reach the current station
            while max_heap and current_fuel < position:
                largest_fuel = -heapq.heappop(max_heap)
                current_fuel += largest_fuel
                stops += 1
            if current_fuel < position:
                return -1
            heapq.heappush(max_heap, -fuel)

        return stops