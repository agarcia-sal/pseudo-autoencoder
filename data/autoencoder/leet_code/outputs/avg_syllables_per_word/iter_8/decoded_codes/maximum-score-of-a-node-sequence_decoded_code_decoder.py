from collections import defaultdict
import heapq

class Solution:
    def maximumScore(self, scores, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for node in graph:
            graph[node] = heapq.nlargest(3, graph[node], key=lambda x: x[0])
        max_score = -1
        for u, v in edges:
            for score1, x in graph.get(u, []):
                for score2, y in graph.get(v, []):
                    if len({x, y, u, v}) == 4:
                        total = score1 + score2 + scores[u] + scores[v]
                        if total > max_score:
                            max_score = total
        return max_score