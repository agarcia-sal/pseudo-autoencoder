class Solution:
    def longestPath(self, parent, s):
        tree = {}
        for index, p in enumerate(parent):
            if p != -1:
                if p not in tree:
                    tree[p] = []
                tree[p].append(index)

        self.result = 1

        def dfs(node):
            max1 = 0
            max2 = 0

            for child in tree.get(node, []):
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