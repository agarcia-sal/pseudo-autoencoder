def max_abs_diff_gain(nums):
    n = len(nums)
    if n == 2:
        return abs(nums[0] - nums[1])

    initial = sum(abs(nums[i] - nums[i-1]) for i in range(1, n))

    max_gain_1 = max(abs(nums[0] - nums[i]) - abs(nums[i] - nums[i-1]) for i in range(1, n))
    max_gain_2 = max(abs(nums[n-1] - nums[i]) - abs(nums[i+1] - nums[i]) for i in range(n-1))
    max_gain = max(max_gain_1, max_gain_2)

    min_pair = min(max(nums[i], nums[i+1]) for i in range(n-1))
    max_pair = max(min(nums[i], nums[i+1]) for i in range(n-1))

    general_gain = max(0, 2 * (max_pair - min_pair))

    return initial + max(max_gain, general_gain)