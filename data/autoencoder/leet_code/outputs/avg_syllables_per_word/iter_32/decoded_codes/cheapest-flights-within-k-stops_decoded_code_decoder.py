import heapq
from typing import List, Dict, Tuple


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build graph as adjacency list: node -> List of (neighbor, weight)
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
        for flight in flights:
            u, v, w = flight
            graph[u].append((v, w))

        # min_heap elements: (cost, stops, city)
        # cost is total cost to reach city, stops is number of edges traveled
        min_heap: List[Tuple[int, int, int]] = [(0, -1, src)]
        # min_cost maps city to minimum number of stops found so far reaching that city
        min_cost: Dict[int, int] = {src: -1}

        while min_heap:
            cost, stops, city = heapq.heappop(min_heap)
            if city == dst:
                return cost
            if stops >= k:
                continue
            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1
                # Push to heap if neighbor not seen before or found path with fewer stops,
                # or if path might be cheaper even with same or more stops
                if neighbor not in min_cost or next_stops < min_cost[neighbor]:
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1