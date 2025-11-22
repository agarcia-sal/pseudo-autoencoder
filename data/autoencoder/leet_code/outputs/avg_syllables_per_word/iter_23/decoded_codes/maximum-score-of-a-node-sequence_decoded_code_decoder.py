from collections import defaultdict
from heapq import nlargest
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for node in graph:
            # Keep only the top 3 neighbors by their score
            graph[node] = nlargest(3, graph[node], key=lambda x: x[0])
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # Ensure all four nodes are distinct
                    if len({x, y, u, v}) == 4:
                        curr = score1 + score2 + scores[u] + scores[v]
                        if curr > max_score:
                            max_score = curr
        return max_score