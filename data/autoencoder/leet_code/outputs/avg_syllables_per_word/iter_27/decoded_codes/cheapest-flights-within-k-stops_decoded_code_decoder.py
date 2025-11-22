from typing import List, Dict, Tuple
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_heap: List[Tuple[int, int, int]] = [(0, -1, src)]  # cost, stops, city
        min_cost: Dict[int, int] = {src: -1}  # city -> stops

        while min_heap:
            cost, stops, city = heapq.heappop(min_heap)

            if city == dst:
                return cost

            if stops >= k:
                continue

            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1

                # Add to heap if this path is strictly better in stops or city not visited with fewer stops
                if (neighbor not in min_cost or next_stops < min_cost[neighbor]) or \
                   (min_heap and next_cost < min_heap[0][0]):
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))

        return -1