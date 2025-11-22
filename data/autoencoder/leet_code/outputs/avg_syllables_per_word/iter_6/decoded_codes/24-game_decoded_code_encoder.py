class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        a, b = nums[i], nums[j]
                        for op in ['+', '*', '-', '/']:
                            if op in ('+', '*') and j > i:
                                continue
                            if op == '+':
                                new_nums.append(a + b)
                            elif op == '*':
                                new_nums.append(a * b)
                            elif op == '-':
                                new_nums.append(a - b)
                            else:  # division
                                if b == 0:
                                    continue
                                new_nums.append(a / b)
                            if solve(new_nums):
                                return True
                            new_nums.pop()
            return False

        return solve(cards)