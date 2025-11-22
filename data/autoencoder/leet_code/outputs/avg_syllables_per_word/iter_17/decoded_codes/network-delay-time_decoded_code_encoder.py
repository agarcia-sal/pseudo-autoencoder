import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.CreateAdjacencyList(times, n)
        dist = self.InitializeDistanceDictionary(n, k)
        min_heap = [(0, k)]

        while min_heap:
            current_dist, node = self.ExtractMinimumFromHeap(min_heap)
            if current_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    self.PushToHeap(min_heap, (distance, neighbor))

        max_time = self.FindMaximumValue(dist)
        if max_time == inf:
            return -1
        else:
            return max_time

    def CreateAdjacencyList(self, times: List[List[int]], n: int) -> List[List[Tuple[int,int]]]:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        return graph

    def InitializeDistanceDictionary(self, n: int, k: int) -> List[float]:
        dist = [inf] * (n + 1)
        dist[k] = 0
        return dist

    def ExtractMinimumFromHeap(self, min_heap: List[Tuple[int,int]]) -> Tuple[int,int]:
        return heapq.heappop(min_heap)

    def PushToHeap(self, min_heap: List[Tuple[int,int]], element: Tuple[int,int]) -> None:
        heapq.heappush(min_heap, element)

    def FindMaximumValue(self, dist: List[float]) -> float:
        return max(dist[1:])