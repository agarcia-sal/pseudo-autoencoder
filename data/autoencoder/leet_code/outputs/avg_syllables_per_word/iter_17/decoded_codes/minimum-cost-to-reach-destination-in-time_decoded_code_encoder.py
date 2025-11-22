import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def minCost(self, maxTime: int, edges: List[Tuple[int, int, int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        priority_queue = [(passingFees[0], 0, 0)]  # (cost, city, time)
        visited_time = [inf] * n
        visited_time[0] = 0

        while priority_queue:
            current_cost, current_city, current_time = heapq.heappop(priority_queue)

            if current_city == n - 1:
                return current_cost

            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                new_cost = current_cost + passingFees[neighbor]

                if new_time <= maxTime and (new_time < visited_time[neighbor] or new_cost < current_cost):
                    visited_time[neighbor] = new_time
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_time))

        return -1