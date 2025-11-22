from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for j in range(3, n - 3):
            seen = set()
            # Check possible i splits before j
            for i in range(1, j - 1):
                left_sum = prefix_sum[i - 1]
                middle_left_sum = prefix_sum[j - 1] - prefix_sum[i]
                if left_sum == middle_left_sum:
                    seen.add(left_sum)
            # Check possible k splits after j
            for k in range(j + 2, n - 1):
                right_sum = prefix_sum[-1] - prefix_sum[k]
                middle_right_sum = prefix_sum[k - 1] - prefix_sum[j]
                if right_sum == middle_right_sum and middle_right_sum in seen:
                    return True

        return False