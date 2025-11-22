from collections import defaultdict
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i, p in enumerate(parent):
            if p != -1:
                tree[p].append(i)

        self_result = 1

        def dfs(node: int) -> int:
            nonlocal self_result
            max_one = 0
            max_two = 0
            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:
                    if child_length > max_one:
                        max_two = max_one
                        max_one = child_length
                    elif child_length > max_two:
                        max_two = child_length
            self_result = max(self_result, max_one + max_two + 1)
            return max_one + 1

        dfs(0)
        return self_result