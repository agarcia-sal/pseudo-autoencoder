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

            for i in range(1, j - 1):
                left_sum = prefix_sum[i - 1]
                mid_left_sum = prefix_sum[j - 1] - prefix_sum[i]
                if left_sum == mid_left_sum:
                    seen.add(left_sum)

            for k in range(j + 2, n - 1):
                right_sum_1 = prefix_sum[k - 1] - prefix_sum[j]
                right_sum_2 = prefix_sum[-1] - prefix_sum[k]
                if right_sum_1 == right_sum_2 and right_sum_1 in seen:
                    return True

        return False