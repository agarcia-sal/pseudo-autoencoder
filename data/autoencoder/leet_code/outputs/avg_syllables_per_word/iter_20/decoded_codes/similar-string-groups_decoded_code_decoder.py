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
            if len(diff) == 0:
                return True
            if len(diff) == 2:
                i1, i2 = diff
                return s1[i1] == s2[i2] and s1[i2] == s2[i1]
            return False

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