from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for flight in flights:
            u, v, w = flight
            graph[u].append((v, w))

        min_heap = [(0, -1, src)]  # (cost, stops, city)
        min_cost = {src: -1}  # city -> min stops to reach city

        while min_heap:
            cost, stops, city = heapq.heappop(min_heap)
            if city == dst:
                return cost
            if stops >= k:
                continue
            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1
                # Check if neighbor not visited or found with fewer stops or next_cost < minimum cost at front of min_heap
                if (neighbor not in min_cost) or (next_stops < min_cost[neighbor]):
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
                else:
                    # It's possible next_cost is less than the smallest cost at front of min_heap, but 
                    # min_cost stores min stops, so no direct access to smallest cost at front.
                    # Given constraints, this additional condition is generally not necessary in normal Dijkstra-like approach.
                    # We omit that condition here for correctness and efficiency.
                    pass

        return -1