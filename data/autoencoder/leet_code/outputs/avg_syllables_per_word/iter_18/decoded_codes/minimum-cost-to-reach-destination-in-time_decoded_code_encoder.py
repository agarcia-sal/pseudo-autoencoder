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

        # Priority queue elements: (cost, city, time)
        pq = [(passingFees[0], 0, 0)]
        visited_time = [inf] * n
        visited_time[0] = 0

        while pq:
            current_cost, current_city, current_time = heapq.heappop(pq)

            if current_city == n - 1:
                return current_cost

            if current_time > visited_time[current_city]:
                # We have already visited this city in less or equal time, skip
                continue

            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                if new_time > maxTime:
                    continue
                new_cost = current_cost + passingFees[neighbor]
                # Only add to queue if arriving sooner, or if cost is better with same or longer time 
                # (the second part handles paths with better cost even if time is not strictly less)
                if new_time < visited_time[neighbor] or new_cost < current_cost:
                    visited_time[neighbor] = new_time
                    heapq.heappush(pq, (new_cost, neighbor, new_time))

        return -1