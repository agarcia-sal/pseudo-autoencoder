from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[0:k])
        sums[0] = current_sum

        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum

        left = [0] * (n - k + 1)
        right = [n - k] * (n - k + 1)

        max_sum = 0
        for i in range(n - k + 1):
            if sums[i] > sums[max_sum]:
                max_sum = i
            left[i] = max_sum

        max_sum = n - k
        for i in range(n - k, -1, -1):
            if sums[i] >= sums[max_sum]:
                max_sum = i
            right[i] = max_sum

        max_total = 0
        result = [0, 0, 0]

        for j in range(k, n - 2 * k + 1):
            i = left[j - k]
            l = right[j + k]
            total = sums[i] + sums[j] + sums[l]
            if total > max_total:
                max_total = total
                result = [i, j, l]

        return result