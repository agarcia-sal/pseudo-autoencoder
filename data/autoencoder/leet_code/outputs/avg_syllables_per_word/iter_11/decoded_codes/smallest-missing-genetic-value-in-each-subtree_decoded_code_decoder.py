from collections import defaultdict

class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        tree = defaultdict(list)

        for index in range(1, n):
            tree[parents[index]].append(index)

        node_with_one = -1
        for index in range(n):
            if nums[index] == 1:
                node_with_one = index
                break

        if node_with_one == -1:
            return [1] * n

        result = [1] * n

        visited = set()

        def dfs(node):
            visited.add(node)
            genetic_values = {nums[node]}
            for child in tree[node]:
                if child not in visited:
                    genetic_values |= dfs(child)
            smallest_missing = 1
            while smallest_missing in genetic_values:
                smallest_missing += 1
            result[node] = smallest_missing
            return genetic_values

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