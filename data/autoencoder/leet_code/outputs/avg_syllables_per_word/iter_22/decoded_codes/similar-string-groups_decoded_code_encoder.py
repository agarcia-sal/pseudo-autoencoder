from collections import defaultdict

class Solution:
    def numSimilarGroups(self, strs):
        def are_similar(s1, s2):
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                if len(diff) > 2:
                    return False
            return (len(diff) == 0) or (
                len(diff) == 2 and
                s1[diff[0]] == s2[diff[1]] and
                s1[diff[1]] == s2[diff[0]]
            )

        def dfs(node, visited):
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