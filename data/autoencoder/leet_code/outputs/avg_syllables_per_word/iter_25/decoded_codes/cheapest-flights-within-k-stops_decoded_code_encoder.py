import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        min_heap = [(0, -1, src)]  # (cost, stops, city)
        min_cost = {src: -1}  # city: min stops to reach
        while min_heap:
            cost, stops, city = heapq.heappop(min_heap)
            if city == dst:
                return cost
            if stops >= k:
                continue
            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1
                # Only push if we can get to neighbor with fewer stops or better cost than what we have seen
                if neighbor not in min_cost or next_stops < min_cost[neighbor] or (min_heap and next_cost < min_heap[0][0]):
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1