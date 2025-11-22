from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximumScore(self, scores: List[int], edges: List[Tuple[int, int]]) -> int:
        graph = defaultdict(list)  # node -> list of (score, index)

        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        for node in graph:
            # Keep only top three neighbors with the highest scores
            graph[node].sort(key=lambda x: x[0], reverse=True)
            graph[node] = graph[node][:3]

        max_score = -1

        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # Check that all four nodes are unique
                    if len({x, y, u, v}) == 4:
                        total = scores[u] + scores[v] + score1 + score2
                        if total > max_score:
                            max_score = total

        return max_score