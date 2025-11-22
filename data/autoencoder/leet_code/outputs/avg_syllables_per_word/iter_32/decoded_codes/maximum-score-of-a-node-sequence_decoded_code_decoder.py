from collections import defaultdict
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        # Build graph with (score, node) pairs for each adjacent node
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        # Keep only top three neighbors by score for each node
        for node in graph:
            graph[node].sort(key=lambda x: x[0], reverse=True)
            graph[node] = graph[node][:3]

        max_score = -1
        for u, v in edges:
            # Try to combine neighbors of u and v while ensuring four distinct nodes
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        candidate = score1 + score2 + scores[u] + scores[v]
                        if candidate > max_score:
                            max_score = candidate
        return max_score