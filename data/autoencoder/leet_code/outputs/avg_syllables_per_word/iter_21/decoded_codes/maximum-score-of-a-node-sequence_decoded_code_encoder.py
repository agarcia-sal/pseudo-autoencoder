from collections import defaultdict

class Solution:
    def maximumScore(self, scores, edges):
        graph = self.create_graph_with_scores(scores, edges)
        self.prune_graph_neighbors(graph)
        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # Check all four nodes are distinct
                    if len({x, y, u, v}) == 4:
                        candidate_score = score1 + score2 + scores[u] + scores[v]
                        if candidate_score > max_score:
                            max_score = candidate_score
        return max_score

    def create_graph_with_scores(self, scores, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        return graph

    def prune_graph_neighbors(self, graph):
        for node in graph.keys():
            # Keep only the top three neighbors by score (descending)
            graph[node] = sorted(graph[node], key=lambda x: x[0], reverse=True)[:3]