import heapq
from math import inf
from typing import List

class Solution:
    def minCost(self, maxTime: int, passingFees: List[int], edges: List[List[int]]) -> int:
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
            # If we have already found a better way to this city at an earlier time, skip
            if current_time > visited_time[current_city]:
                continue
            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                if new_time <= maxTime:
                    new_cost = current_cost + passingFees[neighbor]
                    # Relaxation condition:
                    # Only proceed if we have found a faster arrival time at neighbor,
                    # or a cheaper cost at same or earlier time
                    if new_time < visited_time[neighbor]:
                        visited_time[neighbor] = new_time
                        heapq.heappush(pq, (new_cost, neighbor, new_time))
                    elif new_cost < current_cost:
                        heapq.heappush(pq, (new_cost, neighbor, new_time))
        return -1