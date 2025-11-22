from collections import defaultdict
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        n = len(quiet)
        answer = [-1] * n

        def dfs(person: int) -> int:
            if answer[person] == -1:
                answer[person] = person
                for neighbor in graph[person]:
                    candidate = dfs(neighbor)
                    if quiet[candidate] < quiet[answer[person]]:
                        answer[person] = candidate
            return answer[person]

        for i in range(n):
            dfs(i)
        return answer