from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostKDistinct(t):
            count = defaultdict(int)
            left = 0
            result = 0
            distinct = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                while distinct > t:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result

        return atMostKDistinct(k) - atMostKDistinct(k - 1)