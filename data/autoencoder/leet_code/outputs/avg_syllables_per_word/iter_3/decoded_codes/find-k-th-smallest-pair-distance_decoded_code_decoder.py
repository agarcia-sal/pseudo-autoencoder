from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(mid: int) -> int:
            count = left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left