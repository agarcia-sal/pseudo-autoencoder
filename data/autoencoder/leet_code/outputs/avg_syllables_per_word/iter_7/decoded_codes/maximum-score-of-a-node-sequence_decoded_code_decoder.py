from typing import List, Dict, Tuple
import heapq


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = {}
        for u, v in edges:
            graph.setdefault(u, []).append((scores[v], v))
            graph.setdefault(v, []).append((scores[u], u))

        for node in graph:
            # Keep only the top 3 highest scores for each node
            graph[node] = heapq.nlargest(3, graph[node], key=lambda x: x[0])

        max_score = -1
        for u, v in edges:
            for score1, x in graph.get(u, []):
                for score2, y in graph.get(v, []):
                    if len({x, y, u, v}) == 4:
                        candidate_score = score1 + score2 + scores[u] + scores[v]
                        if candidate_score > max_score:
                            max_score = candidate_score

        return max_score