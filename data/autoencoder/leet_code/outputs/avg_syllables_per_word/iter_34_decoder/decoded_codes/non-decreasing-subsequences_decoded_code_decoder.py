from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited_at_level = set()

        def dfs(u: int, last: int, t: List[int]) -> None:
            if u == len(nums):
                if len(t) > 1:
                    ans.append(t[:])
                return
            if nums[u] >= last and nums[u] not in visited_at_level:
                visited_at_level.add(nums[u])
                t.append(nums[u])
                dfs(u + 1, nums[u], t)
                t.pop()
            # Try skipping current element only if it is different from last chosen element
            dfs(u + 1, last, t)

        dfs(0, float('-inf'), [])
        return ans