from typing import List, Callable
import operator
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            ops: List[Callable[[float, float], float]] = [
                operator.truediv, operator.mul, operator.add, operator.sub
            ]

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in ops:
                            # Skip mirrored cases for commutative ops
                            if (op is operator.add or op is operator.mul) and j > i:
                                continue
                            if op is operator.truediv and nums[j] == 0:
                                continue
                            try:
                                new_elem = op(nums[i], nums[j])
                            except ZeroDivisionError:
                                continue
                            new_nums.append(new_elem)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve([float(c) for c in cards])