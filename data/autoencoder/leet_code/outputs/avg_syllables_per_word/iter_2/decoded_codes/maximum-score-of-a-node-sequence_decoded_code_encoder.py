from collections import defaultdict
from heapq import nlargest

class Solution:
    def maximumScore(self, scores, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))

        for node in graph:
            graph[node] = nlargest(3, graph[node])

        max_score = -1

        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        max_score = max(max_score, score1 + score2 + scores[u] + scores[v])

        return max_score