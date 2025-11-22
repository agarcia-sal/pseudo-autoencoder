from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for node in graph:
            # Keep only the three neighbors with the largest scores
            graph[node] = heapq.nlargest(3, graph[node], key=lambda x: x[0])
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # Ensure all four nodes are distinct
                    if len({x, y, u, v}) == 4:
                        total = score1 + score2 + scores[u] + scores[v]
                        if total > max_score:
                            max_score = total
        return max_score