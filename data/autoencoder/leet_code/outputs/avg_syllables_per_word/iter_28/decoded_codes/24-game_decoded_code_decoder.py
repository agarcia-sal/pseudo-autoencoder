from math import isclose
from operator import add, sub, mul, truediv

class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return isclose(nums[0], 24, abs_tol=1e-6)

            n = len(nums)
            operations = [add, mul, sub, truediv]

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    new_nums = [nums[k] for k in range(n) if k != i and k != j]
                    for op in operations:
                        if (op is add or op is mul) and j > i:
                            continue
                        if (op is truediv and nums[j] == 0):
                            continue
                        try:
                            val = op(nums[i], nums[j])
                        except ZeroDivisionError:
                            continue
                        new_nums.append(val)
                        if solve(new_nums):
                            return True
                        new_nums.pop()
            return False

        return solve(cards)