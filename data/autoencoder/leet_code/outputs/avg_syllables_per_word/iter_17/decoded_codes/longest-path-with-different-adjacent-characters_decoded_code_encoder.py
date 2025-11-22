from collections import defaultdict

class Solution:
    def longestPath(self, parent_list, string_s):
        tree = defaultdict(list)
        for idx, p in enumerate(parent_list):
            if p != -1:
                tree[p].append(idx)

        self_result = 1

        def dfs(node):
            nonlocal self_result
            max1 = 0
            max2 = 0
            for child in tree[node]:
                child_length = dfs(child)
                if string_s[child] != string_s[node]:
                    if child_length > max1:
                        max2 = max1
                        max1 = child_length
                    elif child_length > max2:
                        max2 = child_length
            self_result = max(self_result, max1 + max2 + 1)
            return max1 + 1

        dfs(0)
        return self_result