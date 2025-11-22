from collections import defaultdict
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i, p in enumerate(parent):
            if p != -1:
                tree[p].append(i)

        self.result = 1

        def dfs(node: int) -> int:
            max_path_one = 0
            max_path_two = 0

            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:
                    if child_length > max_path_one:
                        max_path_two = max_path_one
                        max_path_one = child_length
                    elif child_length > max_path_two:
                        max_path_two = child_length

            self.result = max(self.result, max_path_one + max_path_two + 1)
            return max_path_one + 1

        dfs(0)
        return self.result