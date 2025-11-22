from collections import defaultdict
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build adjacency list with (neighbor_score, neighbor_index)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        # Keep only top 3 neighbors by score for each node
        for node in graph:
            graph[node].sort(key=lambda x: x[0], reverse=True)
            graph[node] = graph[node][:3]

        max_score = -1

        # Check combinations for maximum score with distinct nodes
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        total = score1 + score2 + scores[u] + scores[v]
                        if total > max_score:
                            max_score = total

        return max_score