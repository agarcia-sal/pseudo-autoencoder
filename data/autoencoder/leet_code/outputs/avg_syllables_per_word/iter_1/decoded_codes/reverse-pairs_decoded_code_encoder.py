def reversePairs(nums):
    def merge_count(nums, s, e):
        if s >= e:
            return 0
        m = (s + e) // 2
        c = merge_count(nums, s, m) + merge_count(nums, m + 1, e)
        j = m + 1
        for i in range(s, m + 1):
            while j <= e and nums[i] > 2 * nums[j]:
                j += 1
            c += j - (m + 1)
        merged = []
        l, r = s, m + 1
        while l <= m and r <= e:
            if nums[l] <= nums[r]:
                merged.append(nums[l])
                l += 1
            else:
                merged.append(nums[r])
                r += 1
        merged.extend(nums[l:m + 1])
        merged.extend(nums[r:e + 1])
        nums[s:e + 1] = merged
        return c

    return merge_count(nums, 0, len(nums) - 1)