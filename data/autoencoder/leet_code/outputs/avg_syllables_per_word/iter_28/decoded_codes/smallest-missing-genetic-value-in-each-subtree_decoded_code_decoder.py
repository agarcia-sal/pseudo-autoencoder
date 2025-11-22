from collections import defaultdict
from typing import List

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        tree = defaultdict(list)

        for i in range(1, n):
            tree[parents[i]].append(i)

        node_with_one = -1
        for i in range(n):
            if nums[i] == 1:
                node_with_one = i
                break

        if node_with_one == -1:
            return [1] * n

        result = [1] * n

        visited = set()

        def dfs(node: int) -> set:
            visited.add(node)
            genetic_values = {nums[node]}
            for child in tree[node]:
                if child not in visited:
                    genetic_values |= dfs(child)
            smallest_missing = 1
            # Find the smallest missing positive integer in genetic_values
            while smallest_missing in genetic_values:
                smallest_missing += 1
            result[node] = smallest_missing
            return genetic_values

        path = []
        current = node_with_one
        while current != -1:
            path.append(current)
            current = parents[current]

        path_set = set(path)  # Not explicitly required but kept for clarity

        for node in reversed(path):
            if node in visited:
                continue
            dfs(node)

        return result