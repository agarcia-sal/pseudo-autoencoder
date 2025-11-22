from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostKDistinct(t):
            count = defaultdict(int)
            left = result = 0
            for right, val in enumerate(nums):
                count[val] += 1
                while len(count) > t:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result

        return atMostKDistinct(k) - atMostKDistinct(k - 1)