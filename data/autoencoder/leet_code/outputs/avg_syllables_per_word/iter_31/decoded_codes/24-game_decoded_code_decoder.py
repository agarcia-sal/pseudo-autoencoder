from operator import add, sub, mul, truediv
from typing import List

class Solution:
    def judgePoint24(self, cards: List[float]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            length = len(nums)
            for i in range(length):
                for j in range(length):
                    if i != j:
                        new_nums = [nums[k] for k in range(length) if k != i and k != j]

                        for op in (truediv, mul, add, sub):
                            if op in (add, mul) and j > i:
                                continue
                            if op is truediv and nums[j] == 0:
                                continue

                            new_nums.append(op(nums[i], nums[j]))
                            if solve(new_nums):
                                return True
                            new_nums.pop()

            return False

        return solve(cards)