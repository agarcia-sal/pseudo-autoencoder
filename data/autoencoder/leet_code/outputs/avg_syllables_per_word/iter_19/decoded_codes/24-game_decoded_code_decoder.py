import operator
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)
            ops = [operator.truediv, operator.mul, operator.add, operator.sub]

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    new_nums = [nums[k] for k in range(n) if k != i and k != j]

                    for op in ops:
                        # Skip duplicate addition/multiplication on swapped pairs to reduce redundant computations
                        if (op is operator.add or op is operator.mul) and j > i:
                            continue

                        if op is operator.truediv and abs(nums[j]) < 1e-12:
                            continue  # Avoid division by zero

                        val = op(nums[i], nums[j])
                        new_nums.append(val)
                        if solve(new_nums):
                            return True
                        new_nums.pop()
            return False

        return solve([float(c) for c in cards])