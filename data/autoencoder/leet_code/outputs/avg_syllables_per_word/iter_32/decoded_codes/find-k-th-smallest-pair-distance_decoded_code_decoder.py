from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(mid: int) -> int:
            cnt = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                cnt += right - left
            return cnt

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left