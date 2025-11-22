from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        new_nums = [nums[k] for k in range(n) if k != i and k != j]

                        a, b = nums[i], nums[j]
                        # addition
                        if j <= i:
                            new_nums.append(a + b)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
                        # multiplication
                        if j <= i:
                            new_nums.append(a * b)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
                        # subtraction
                        new_nums.append(a - b)
                        if solve(new_nums):
                            return True
                        new_nums.pop()
                        # division
                        if abs(b) > 1e-12:
                            new_nums.append(a / b)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        cards_float = [float(c) if c is not None else None for c in cards]
        # Remove None if any encountered (though problem likely doesn't have)
        if any(c is None for c in cards_float):
            return False

        return solve(cards_float)