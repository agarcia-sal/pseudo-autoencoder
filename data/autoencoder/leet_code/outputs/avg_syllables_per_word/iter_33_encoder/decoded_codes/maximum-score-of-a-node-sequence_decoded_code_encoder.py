from collections import defaultdict
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for node in graph:
            # Keep only top 3 neighbors with highest scores
            graph[node] = sorted(graph[node], key=lambda x: x[0], reverse=True)[:3]
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        total = score1 + score2 + scores[u] + scores[v]
                        if total > max_score:
                            max_score = total
        return max_score