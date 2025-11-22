from typing import List
import operator
import math

class Solution:
    def judgePoint24(self, cards: List[float]) -> bool:
        # Tolerance for floating point comparison
        EPS = 1e-6
        # Operations to try: true division, multiplication, addition, subtraction
        ops = [
            operator.truediv,
            operator.mul,
            operator.add,
            operator.sub,
        ]

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return math.isclose(nums[0], 24, abs_tol=EPS)

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        # Build new list excluding nums[i], nums[j]
                        new_nums = [nums[k] for k in range(n) if k != i and k != j]
                        for op_idx, op in enumerate(ops):
                            # Skip repeated permutations for commutative operations (addition, multiplication)
                            # only allow (i,j) with i > j to avoid duplicate checks
                            if (op == operator.add or op == operator.mul) and j > i:
                                continue

                            a = nums[i]
                            b = nums[j]
                            # Avoid division by zero
                            if op == operator.truediv and abs(b) < EPS:
                                continue
                            try:
                                val = op(a, b)
                            except ZeroDivisionError:
                                continue  # Just in case, though we check above
                            new_nums.append(val)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve(cards)