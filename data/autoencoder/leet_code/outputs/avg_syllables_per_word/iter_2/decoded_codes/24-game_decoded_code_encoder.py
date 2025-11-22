from typing import List
import math
import operator

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return math.isclose(nums[0], 24, abs_tol=1e-6)

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in (operator.truediv, operator.mul, operator.add, operator.sub):
                            if (op is operator.add or op is operator.mul) and j > i:
                                continue

                            if op is not operator.truediv or nums[j] != 0:
                                new_nums.append(op(nums[i], nums[j]))
                                if solve(new_nums):
                                    return True
                                new_nums.pop()
            return False

        return solve(cards)