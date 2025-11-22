def three_sum_closest(nums, target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums) - 2):
        L, R = i + 1, len(nums) - 1
        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                L += 1
            elif s > target:
                R -= 1
            else:
                return s
    return closest