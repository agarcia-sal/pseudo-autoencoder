from collections import defaultdict
import heapq
from typing import List, Tuple

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = self.create_default_dictionary_of_lists()
        for u, v in edges:
            self.APPEND_pair_to_graph_with_scores(graph, u, v, scores)

        for node in graph:
            graph[node] = self.select_top_three_elements(graph[node])

        max_score = -1
        for u, v in edges:
            for score1, x in graph[u]:
                for score2, y in graph[v]:
                    # nodes x, y, u, v must be distinct
                    if len({x, y, u, v}) == 4:
                        sum_score = score1 + score2 + scores[u] + scores[v]
                        if sum_score > max_score:
                            max_score = sum_score

        return max_score

    def create_default_dictionary_of_lists(self) -> defaultdict:
        return defaultdict(list)

    def APPEND_pair_to_graph_with_scores(self, graph: defaultdict, u: int, v: int, scores: List[int]) -> None:
        # Append (score, node) pairs to the adjacency lists for both ends (undirected graph)
        graph[u].append((scores[v], v))
        graph[v].append((scores[u], u))

    def select_top_three_elements(self, collection: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # Extract top 3 elements with highest scores using a max-heap approach
        # heapq in python is a min-heap, so invert scores to get max-heap behavior
        if len(collection) <= 3:
            # just return sorted descending by score
            return sorted(collection, key=lambda x: x[0], reverse=True)

        # Use nlargest to efficiently get top 3
        return heapq.nlargest(3, collection, key=lambda x: x[0])