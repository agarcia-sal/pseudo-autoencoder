from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)  # node -> List[Tuple[score, node]]

        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        for node in graph:
            graph[node].sort(key=lambda x: x[0], reverse=True)
            graph[node] = graph[node][:3]

        max_score = -1

        for u, v in edges:
            su, sv = scores[u], scores[v]
            for score1, x in graph[u]:
                if x == u or x == v:
                    continue
                for score2, y in graph[v]:
                    if y == u or y == v or y == x:
                        continue
                    total_unique = {x, y, u, v}
                    if len(total_unique) == 4:
                        current_score = score1 + score2 + su + sv
                        if current_score > max_score:
                            max_score = current_score

        return max_score