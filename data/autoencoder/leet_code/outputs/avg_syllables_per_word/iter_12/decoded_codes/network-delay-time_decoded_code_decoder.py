import heapq
import math

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = self.initialize_graph(n)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = self.initialize_distances(n, k)
        min_heap = self.initialize_min_heap(k)

        while min_heap:
            current_dist, node = self.pop_minimum(min_heap)

            if current_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    self.push_minimum(min_heap, (distance, neighbor))

        max_time = self.maximum_value(dist.values())
        if max_time == math.inf:
            return -1
        else:
            return max_time

    def initialize_graph(self, n):
        graph = {}
        for index in range(1, n + 1):
            graph[index] = []
        return graph

    def initialize_distances(self, n, k):
        dist = {}
        for index in range(1, n + 1):
            dist[index] = math.inf
        dist[k] = 0
        return dist

    def initialize_min_heap(self, k):
        return [(0, k)]

    def pop_minimum(self, min_heap):
        return heapq.heappop(min_heap)

    def push_minimum(self, min_heap, pair):
        heapq.heappush(min_heap, pair)

    def maximum_value(self, collection):
        max_value = -math.inf
        for value in collection:
            if value > max_value:
                max_value = value
        return max_value