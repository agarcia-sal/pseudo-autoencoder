import heapq
from math import inf
from typing import List

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        pq = [(passingFees[0], 0, 0)]  # (cost, city, time)
        visited_time = [inf] * n
        visited_time[0] = 0

        while pq:
            current_cost, current_city, current_time = heapq.heappop(pq)
            if current_city == n - 1:
                return current_cost

            if current_time > visited_time[current_city]:
                continue  # Already found a faster way to this city

            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                if new_time <= maxTime:
                    new_cost = current_cost + passingFees[neighbor]
                    # Accept path if found earlier time, or better cost at same or earlier time
                    if new_time < visited_time[neighbor]:
                        visited_time[neighbor] = new_time
                        heapq.heappush(pq, (new_cost, neighbor, new_time))
                    elif new_cost < current_cost:
                        # Push also if new cost is strictly less, even if time is not better
                        heapq.heappush(pq, (new_cost, neighbor, new_time))

        return -1