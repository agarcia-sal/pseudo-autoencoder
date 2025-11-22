from typing import List

class Solution:
    def stoneGameVIII(self, list_of_stones: List[int]) -> int:
        n = len(list_of_stones)
        prefix_sum = [0] * n
        prefix_sum[0] = list_of_stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + list_of_stones[i]

        dp = prefix_sum[-1]
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix_sum[i] - dp)
        return dp