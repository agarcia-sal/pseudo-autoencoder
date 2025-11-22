from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countPairs(self, n, edges, queries):
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        shared = defaultdict(int)
        for u, v in edges:
            if u > v:
                u, v = v, u
            shared[(u, v)] += 1

        sorted_degree = sorted(degree[1:])

        answers = []
        for q in queries:
            count = 0
            left, right = 0, n - 1
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > q:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            for (u, v), c in shared.items():
                total = degree[u] + degree[v]
                if total > q and total - c <= q:
                    count -= 1

            answers.append(count)

        return answers