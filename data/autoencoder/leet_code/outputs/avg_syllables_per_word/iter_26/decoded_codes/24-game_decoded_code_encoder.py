from operator import truediv, mul, add, sub

class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        for op in (add, mul, sub, truediv):
                            if (op is add or op is mul) and j > i:
                                continue
                            if op is not truediv or nums[j] != 0:
                                new_nums.append(op(nums[i], nums[j]))
                                if solve(new_nums):
                                    return True
                                new_nums.pop()
            return False

        return solve(cards)