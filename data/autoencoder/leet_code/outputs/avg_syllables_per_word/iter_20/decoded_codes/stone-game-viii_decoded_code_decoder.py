from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix_sum = [0] * len(stones)
        prefix_sum[0] = stones[0]
        for i in range(1, len(stones)):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i]

        dp = prefix_sum[-1]
        for i in range(len(stones) - 2, 0, -1):
            candidate = prefix_sum[i] - dp
            if dp >= candidate:
                # dp remains the same
                continue
            else:
                dp = candidate
        return dp