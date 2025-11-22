import operator
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        TARGET = 24

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON

            length = len(nums)
            for i in range(length):
                for j in range(length):
                    if i != j:
                        new_nums = [nums[k] for k in range(length) if k != i and k != j]
                        a, b = nums[i], nums[j]

                        # Addition and multiplication are commutative:
                        # To avoid duplicates, for + and *, only proceed if j <= i
                        # skip if j > i for these operations
                        operations = [
                            ('+', operator.add),
                            ('-', operator.sub),
                            ('*', operator.mul),
                            ('/', operator.truediv),
                        ]
                        for op_symbol, op_func in operations:
                            if (op_symbol in ('+', '*') and j > i):
                                continue
                            if op_symbol == '/' and abs(b) < EPSILON:
                                continue

                            try:
                                val = op_func(a, b)
                            except ZeroDivisionError:
                                continue

                            new_nums.append(val)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve([float(c) for c in cards])