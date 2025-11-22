from collections import defaultdict
import heapq

class Solution:
    def maximumScore(self, scores, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        # Keep only top three neighbors by score for each node
        for node in graph:
            graph[node] = heapq.nlargest(3, graph[node], key=lambda x: x[0])
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    if len({x, y, u, v}) == 4:
                        current_score = score1 + score2 + scores[u] + scores[v]
                        if current_score > max_score:
                            max_score = current_score
        return max_score