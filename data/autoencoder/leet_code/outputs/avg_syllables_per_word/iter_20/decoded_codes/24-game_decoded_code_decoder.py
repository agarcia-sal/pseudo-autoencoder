from operator import truediv, mul, add, sub
from math import isclose

class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return isclose(nums[0], 24, abs_tol=1e-6)
            length = len(nums)
            for i in range(length):
                for j in range(length):
                    if i != j:
                        new_nums = [nums[k] for k in range(length) if k != i and k != j]
                        for op in (add, mul, sub, truediv):
                            # Skip duplicate calculations for commutative ops when j > i
                            if (op is add or op is mul) and j > i:
                                continue
                            if op is truediv and nums[j] == 0:
                                continue
                            val = op(nums[i], nums[j])
                            new_nums.append(val)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve(cards)