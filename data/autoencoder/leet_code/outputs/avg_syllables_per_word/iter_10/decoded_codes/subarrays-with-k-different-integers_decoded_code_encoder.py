class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostKDistinct(t):
            count = {}
            left = result = 0
            for right, x in enumerate(nums):
                count[x] = count.get(x, 0) + 1
                while len(count) > t:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result

        return atMostKDistinct(k) - atMostKDistinct(k - 1)