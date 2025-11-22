class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        new_nums = [nums[k] for k in range(n) if k != i and k != j]
                        for op in (lambda a, b: a + b,
                                   lambda a, b: a * b,
                                   lambda a, b: a - b,
                                   lambda a, b: a / b if b != 0 else None):
                            if (op == (lambda a,b: a + b) or op == (lambda a,b: a * b)) and j > i:
                                continue
                            val = op(nums[i], nums[j])
                            if val is not None:
                                new_nums.append(val)
                                if solve(new_nums):
                                    return True
                                new_nums.pop()
            return False

        return solve(cards)