import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

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
                # The pseudocode condition is slightly ambiguous,
                # but translating literally: 
                # if neighbor not in min_cost or next_stops < min_cost[neighbor] 
                #    or next_cost < first element of first tuple in min_heap
                # Since min_heap can be empty after heappop, check that.

                # The pseudocode's last condition (next_cost < min_heap[0][0]) is unusual,
                # but we will implement it as stated.
                heap_first_cost = min_heap[0][0] if min_heap else float('inf')

                if (neighbor not in min_cost or next_stops < min_cost[neighbor] or next_cost < heap_first_cost):
                    min_cost[neighbor] = next_stops
                    heapq.heappush(min_heap, (next_cost, next_stops, neighbor))

        return -1