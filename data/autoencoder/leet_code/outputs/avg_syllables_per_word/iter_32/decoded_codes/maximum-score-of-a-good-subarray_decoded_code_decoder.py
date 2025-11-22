from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        current_min = nums[k]
        max_score = current_min

        n = len(nums)

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] >= nums[right + 1]:
                left -= 1
            else:
                right += 1

            current_min = min(current_min, nums[left], nums[right])
            length = right - left + 1
            score = current_min * length
            if score > max_score:
                max_score = score

        return max_score