from typing import List, Tuple
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[Tuple[int,int,int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        # Elements in min_heap: (cost so far, stops so far, current city)
        min_heap = [(0, -1, src)]
        # min_cost maps city to the minimum number of stops seen so far to reach it
        min_cost = {src: -1}

        while min_heap:
            cost, stops, city = heapq.heappop(min_heap)
            if city == dst:
                return cost
            if stops >= k:
                continue
            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1
                # Only proceed if neighbor not visited with fewer stops or found cheaper
                if (neighbor not in min_cost
                    or next_stops < min_cost[neighbor]
                    or (min_heap and next_cost < min_heap[0][0])):
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1