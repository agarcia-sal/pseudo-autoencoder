import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_heap = [(0, -1, src)]  # cost, stops, city
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
                if neighbor not in min_cost or next_stops < min_cost[neighbor]:
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1