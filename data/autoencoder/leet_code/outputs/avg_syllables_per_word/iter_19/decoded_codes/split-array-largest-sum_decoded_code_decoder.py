from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            current_sum = 0
            subarrays = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:  # early exit if too many subarrays
                        return False
                else:
                    current_sum += num
            return subarrays <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left