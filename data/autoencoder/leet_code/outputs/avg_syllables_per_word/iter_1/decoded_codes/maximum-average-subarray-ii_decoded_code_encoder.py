def findMaxAverage(nums, k):
    def canFindAverage(mid):
        prefix_sums = [0] * (len(nums) + 1)
        min_prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i] - mid
            if i >= k:
                min_prefix_sum[i + 1] = min(min_prefix_sum[i], prefix_sums[i + 1 - k])
            else:
                min_prefix_sum[i + 1] = min_prefix_sum[i]

            if i >= k - 1 and prefix_sums[i + 1] - min_prefix_sum[i + 1] >= 0:
                return True
        return False

    low, high = min(nums), max(nums)
    while high - low > 1e-5:
        mid = (low + high) / 2
        if canFindAverage(mid):
            low = mid
        else:
            high = mid
    return low