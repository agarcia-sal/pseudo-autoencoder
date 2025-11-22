import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # heap entries: (cost, stops, city)
        min_heap = [(0, -1, src)]
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
                # We push to heap if neighbor never visited or we found a route with fewer stops
                # The extra condition from pseudocode "or next_cost < cost at min_heap[0]" is omitted here as
                # heapq structure doesn't directly expose the minimal cost of some city in heap; it is not typical
                # Instead, we track minimal stops to prune
                if neighbor not in min_cost or next_stops < min_cost[neighbor]:
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1