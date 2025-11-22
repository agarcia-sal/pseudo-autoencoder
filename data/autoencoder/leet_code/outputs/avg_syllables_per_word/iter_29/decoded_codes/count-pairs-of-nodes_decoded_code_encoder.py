from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        shared = defaultdict(int)
        for u, v in edges:
            if u > v:
                u, v = v, u
            shared[(u, v)] += 1

        sorted_degree = sorted(degree[1:])  # Ignore degree[0] since nodes are 1-indexed

        answers = []
        for q in queries:
            count = 0
            left, right = 0, n - 1  # zero-based indexing for sorted_degree
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > q:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            for (u, v), count_uv in shared.items():
                deg_sum = degree[u] + degree[v]
                if deg_sum > q >= deg_sum - count_uv:
                    count -= 1

            answers.append(count)

        return answers