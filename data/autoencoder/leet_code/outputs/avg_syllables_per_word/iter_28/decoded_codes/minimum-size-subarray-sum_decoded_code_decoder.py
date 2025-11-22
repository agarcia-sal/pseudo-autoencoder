from math import inf
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = inf
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                if min_length > right - left + 1:
                    min_length = right - left + 1
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != inf else 0