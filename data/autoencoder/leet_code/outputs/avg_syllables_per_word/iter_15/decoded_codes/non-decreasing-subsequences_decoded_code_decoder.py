from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

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

        dfs(0, -1000, [])
        # Deduplicate since the pseudocode can add duplicates due to branching
        # Using set with tuples because lists are unhashable
        seen = set()
        unique_ans = []
        for seq in ans:
            t_seq = tuple(seq)
            if t_seq not in seen:
                seen.add(t_seq)
                unique_ans.append(seq)
        return unique_ans