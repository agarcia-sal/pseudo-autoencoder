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
            max1, max2 = 0, 0
            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:
                    if child_length > max1:
                        max2 = max1
                        max1 = child_length
                    elif child_length > max2:
                        max2 = child_length
            self.result = max(self.result, max1 + max2 + 1)
            return max1 + 1

        dfs(0)
        return self.result