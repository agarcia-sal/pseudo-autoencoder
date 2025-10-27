class Solution:
    def findSubsequences(self, nums):
        def dfs(u, last, t):
            if u == len(nums):
                if len(t) > 1:
                    ans.append(t[:])
                return
            if nums[u] >= last:
                t.append(nums[u])
                dfs(u + 1, nums[u], t)
                t.pop()
            if nums[u] != last:
                dfs(u + 1, last, t)

        ans = []
        dfs(0, float('-inf'), [])
        # Remove duplicates since the approach might add duplicates due to handling equal numbers separately
        res = []
        seen = set()
        for seq in ans:
            tup = tuple(seq)
            if tup not in seen:
                seen.add(tup)
                res.append(seq)
        return res