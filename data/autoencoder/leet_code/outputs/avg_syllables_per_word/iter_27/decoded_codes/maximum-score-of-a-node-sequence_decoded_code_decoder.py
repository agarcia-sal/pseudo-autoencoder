from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for node in graph:
            graph[node] = sorted(graph[node], key=lambda x: x[0], reverse=True)[:3]
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        candidate_score = score1 + score2 + scores[u] + scores[v]
                        if candidate_score > max_score:
                            max_score = candidate_score
        return max_score