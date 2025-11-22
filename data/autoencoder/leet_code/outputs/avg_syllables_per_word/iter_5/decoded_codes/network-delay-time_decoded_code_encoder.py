import heapq
import math

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: math.inf for i in range(1, n+1)}
        dist[k] = 0

        min_heap = [(0, k)]
        while min_heap:
            current_dist, node = heapq.heappop(min_heap)
            if current_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        max_time = max(dist.values())
        return -1 if max_time == math.inf else max_time