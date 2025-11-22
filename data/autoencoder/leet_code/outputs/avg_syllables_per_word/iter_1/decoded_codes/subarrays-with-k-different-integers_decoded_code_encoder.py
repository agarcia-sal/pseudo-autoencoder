def subarraysWithKDistinct(nums, k):
    def atMostKDistinct(t):
        count = {}
        left = 0
        res = 0
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) > t:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += right - left + 1
        return res
    return atMostKDistinct(k) - atMostKDistinct(k - 1)