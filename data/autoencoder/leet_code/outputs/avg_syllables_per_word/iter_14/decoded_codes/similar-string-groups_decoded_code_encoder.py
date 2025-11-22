from collections import defaultdict
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def are_similar(s1: str, s2: str) -> bool:
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
            if len(diff) == 0:
                return True
            if len(diff) == 2:
                i1, i2 = diff[0], diff[1]
                return s1[i1] == s2[i2] and s1[i2] == s2[i1]
            return False

        def dfs(node: int, visited: set):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        n = len(strs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        num_groups = 0
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                num_groups += 1

        return num_groups