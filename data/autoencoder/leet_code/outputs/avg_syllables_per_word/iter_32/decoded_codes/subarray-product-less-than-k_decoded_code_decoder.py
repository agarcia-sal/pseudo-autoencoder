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
                product //= nums[left] if product % nums[left] == 0 else product / nums[left]
                # Using float division if necessary to avoid float rounding errors
                # But in practice, all nums[right] are positive integers, so integer division suffices if exact
                left += 1

            count += right - left + 1

        return count