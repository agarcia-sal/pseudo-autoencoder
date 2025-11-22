import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = []
        current_fuel = startFuel
        stops = 0
        stations.append([target, 0])

        for position, fuel in stations:
            while max_heap and current_fuel < position:
                current_fuel += -heapq.heappop(max_heap)  # pop largest fuel from heap (stored as negative)
                stops += 1
            if current_fuel < position:
                return -1
            heapq.heappush(max_heap, -fuel)  # push negative fuel to maintain max-heap behavior

        return stops