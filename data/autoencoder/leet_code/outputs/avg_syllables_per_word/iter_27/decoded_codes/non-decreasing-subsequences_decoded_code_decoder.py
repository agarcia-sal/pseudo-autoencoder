from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(u: int, last: int, t: List[int]) -> None:
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

        ans: List[List[int]] = []
        dfs(0, -1000, [])
        return ans