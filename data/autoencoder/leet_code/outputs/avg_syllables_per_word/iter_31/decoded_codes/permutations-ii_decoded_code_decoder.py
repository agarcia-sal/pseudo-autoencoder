from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], used: List[bool], res: List[List[int]]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used, res)
                path.pop()
                used[i] = False

        nums.sort()
        res: List[List[int]] = []
        used: List[bool] = [False] * len(nums)
        backtrack([], used, res)
        return res