import heapq
from math import inf

class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]

        # Build graph adjacency list: graph[node] = [(neighbor, travel_time), ...]
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        # Priority queue elements: (current_cost, current_city, current_time)
        priority_queue = [(passingFees[0], 0, 0)]
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