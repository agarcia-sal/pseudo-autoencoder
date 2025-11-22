from collections import defaultdict

class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parents[i]].append(i)

        node_with_one = -1
        for i, val in enumerate(nums):
            if val == 1:
                node_with_one = i
                break

        if node_with_one == -1:
            return [1] * n

        result = [1] * n
        visited = set()

        def dfs(node):
            visited.add(node)
            values = {nums[node]}
            for child in tree[node]:
                if child not in visited:
                    values |= dfs(child)
            smallest_missing = 1
            while smallest_missing in values:
                smallest_missing += 1
            result[node] = smallest_missing
            return values

        path = []
        current = node_with_one
        while current != -1:
            path.append(current)
            current = parents[current]
        path_set = set(path)

        for node in reversed(path):
            if node in visited:
                continue
            dfs(node)

        return result