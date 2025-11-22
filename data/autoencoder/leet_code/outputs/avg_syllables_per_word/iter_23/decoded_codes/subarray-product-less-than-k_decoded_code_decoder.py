from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left] if nums[left] != 0 else 1  # Handle zero gracefully
                left += 1

            count += right - left + 1

        return count