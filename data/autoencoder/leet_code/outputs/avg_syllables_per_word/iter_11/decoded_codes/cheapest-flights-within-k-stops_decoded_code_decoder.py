from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        min_heap = [(0, -1, src)]
        min_cost = {src: -1}

        while min_heap:
            cost, stops, city = heappop(min_heap)
            if city == dst:
                return cost
            if stops >= k:
                continue
            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1
                if (neighbor not in min_cost or
                    next_stops < min_cost[neighbor] or
                    (min_heap and next_cost < min_heap[0][0])):
                    min_cost[neighbor] = next_stops
                    heappush(min_heap, (next_cost, next_stops, neighbor))
        return -1