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
            for i in range(1, j):
                if prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]:
                    seen.add(prefix_sum[i - 1])
            for k in range(j + 2, n - 1):
                part1 = prefix_sum[n - 1] - prefix_sum[k]
                part2 = prefix_sum[k - 1] - prefix_sum[j]
                if part1 == part2 and part2 in seen:
                    return True
        return False