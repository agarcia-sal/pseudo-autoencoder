from typing import List

class Solution:
    def search(self, nums: List[int], TARGET: int) -> bool:
        if len(nums) == 0:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == TARGET:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= TARGET < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < TARGET <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False