from collections import defaultdict
from heapq import nlargest
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        # Build graph with (score, node) pairs
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        # Keep only the top three highest score neighbors per node
        for node in graph:
            graph[node] = nlargest(3, graph[node], key=lambda x: x[0])

        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # Check that all four nodes are distinct
                    if len({x, y, u, v}) == 4:
                        total = score1 + score2 + scores[u] + scores[v]
                        if total > max_score:
                            max_score = total
        return max_score