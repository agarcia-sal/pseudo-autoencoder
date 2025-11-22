from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(t: int) -> int:
            count = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                while len(count) > t:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result

        if k == 0:
            return 0
        return atMostKDistinct(k) - atMostKDistinct(k - 1)