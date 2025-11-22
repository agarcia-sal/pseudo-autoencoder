def smallest_distance_pair(nums, k):
    nums.sort()
    n = len(nums)

    def count(d):
        c = 0
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > d:
                l += 1
            c += r - l
        return c

    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = (l + r) // 2
        if count(m) < k:
            l = m + 1
        else:
            r = m

    return l