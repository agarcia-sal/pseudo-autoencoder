from typing import List, Set, Dict

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(s1: str, s2: str) -> bool:
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if len(diff) == 0:
                return True
            if len(diff) == 2:
                i, j = diff
                return s1[i] == s2[j] and s1[j] == s2[i]
            return False

        def dfs(node: int, visited: Set[int]) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        n = len(strs)
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited: Set[int] = set()
        num_groups = 0

        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                num_groups += 1

        return num_groups