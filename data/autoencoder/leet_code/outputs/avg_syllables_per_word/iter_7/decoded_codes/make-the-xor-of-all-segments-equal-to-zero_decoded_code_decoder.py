from typing import List
from collections import defaultdict

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        groups = defaultdict(list)
        for i in range(len(nums)):
            groups[i % k].append(nums[i])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [float('inf')] * k
        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        max_mask = 1 << 10  # 2^10
        dp = [float('inf')] * max_mask
        dp[0] = 0

        for i in range(k):
            new_dp = [float('inf')] * max_mask
            min_dp = min(dp)
            for j in range(max_mask):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    new_dp[j] = min(new_dp[j], dp[j ^ num] + min_size[i] - count)
            dp = new_dp

        return dp[0]