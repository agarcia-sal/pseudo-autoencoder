from operator import truediv, mul, add, sub
from typing import List

class Solution:
    def judgePoint24(self, cards: List[float]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                # Check if the single number is close enough to 24 within a tolerance
                return abs(nums[0] - 24) < 1e-6

            length = len(nums)
            for i in range(length):
                for j in range(length):
                    if i != j:
                        new_nums = [nums[k] for k in range(length) if k != i and k != j]

                        for op in (add, sub, mul, truediv):
                            # Skip repeated cases by ordering addition and multiplication operands
                            if (op == add or op == mul) and j > i:
                                continue
                            # Skip division by zero
                            if op == truediv and nums[j] == 0:
                                continue

                            try:
                                result = op(nums[i], nums[j])
                            except ZeroDivisionError:
                                continue

                            new_nums.append(result)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve(cards)