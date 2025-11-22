def max_sum_of_three_subarrays(nums, k):
    n = len(nums)
    sums = [0] * (n - k + 1)
    sums[0] = sum(nums[0:k])
    for i in range(1, n - k + 1):
        sums[i] = sums[i - 1] + nums[i + k - 1] - nums[i - 1]

    left = [0] * (n - k + 1)
    max_i = 0
    for i in range(n - k + 1):
        if sums[i] > sums[max_i]:
            max_i = i
        left[i] = max_i

    right = [0] * (n - k + 1)
    max_i = n - k
    for i in range(n - k, -1, -1):
        if sums[i] >= sums[max_i]:
            max_i = i
        right[i] = max_i

    max_total = 0
    res = [0, 0, 0]
    for j in range(k, n - 2 * k + 1):
        i = left[j - k]
        l = right[j + k]
        total = sums[i] + sums[j] + sums[l]
        if total > max_total:
            max_total = total
            res = [i, j, l]

    return res