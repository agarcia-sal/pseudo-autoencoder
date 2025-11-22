def searchRange(nums, target):
    def find_left(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l

    def find_right(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return r

    L = find_left(nums, target)
    R = find_right(nums, target)
    if L <= R and 0 <= R < len(nums) and nums[L] == target:
        return [L, R]
    else:
        return [-1, -1]