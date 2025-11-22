from typing import List, Dict, Set

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        tree: Dict[int, List[int]] = {i: [] for i in range(n)}
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
        visited: Set[int] = set()

        def dfs(node: int) -> Set[int]:
            visited.add(node)
            genetic_values = {nums[node]}
            for child in tree[node]:
                if child not in visited:
                    child_genetic_values = dfs(child)
                    genetic_values.update(child_genetic_values)

            smallest_missing = 1
            while smallest_missing in genetic_values:
                smallest_missing += 1
            result[node] = smallest_missing
            return genetic_values

        path: List[int] = []
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