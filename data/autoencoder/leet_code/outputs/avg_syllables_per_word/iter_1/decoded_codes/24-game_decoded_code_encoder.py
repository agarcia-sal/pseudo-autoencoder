def judgePoint24(cards):
    def solve(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for op in (lambda x, y: x + y,
                               lambda x, y: x - y,
                               lambda x, y: x * y,
                               lambda x, y: x / y if y != 0 else None):
                        if (op in (lambda x, y: x + y, lambda x, y: x * y)) and j > i:
                            continue
                        res = op(nums[i], nums[j])
                        if res is None:
                            continue
                        new_nums.append(res)
                        if solve(new_nums):
                            return True
                        new_nums.pop()
        return False
    return solve(cards)