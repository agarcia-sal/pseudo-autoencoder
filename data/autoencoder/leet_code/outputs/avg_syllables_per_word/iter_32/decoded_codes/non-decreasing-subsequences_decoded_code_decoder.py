from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(u: int, last: int, t: List[int]):
            if u == len(nums):
                if len(t) > 1:
                    ans.append(t[:])  # Append a copy of t
                return
            if nums[u] >= last:
                t.append(nums[u])
                dfs(u + 1, nums[u], t)
                t.pop()
            if nums[u] != last:
                dfs(u + 1, last, t)

        dfs(0, -1000, [])
        return ans