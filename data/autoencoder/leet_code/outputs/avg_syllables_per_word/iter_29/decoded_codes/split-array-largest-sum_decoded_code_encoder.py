from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            current_sum = 0
            subarrays = 1
            for number in nums:
                if current_sum + number > max_sum:
                    subarrays += 1
                    current_sum = number
                else:
                    current_sum += number
            return subarrays <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left