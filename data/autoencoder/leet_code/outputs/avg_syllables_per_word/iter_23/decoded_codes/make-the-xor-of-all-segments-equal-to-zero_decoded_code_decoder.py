from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        groups = defaultdict(list)
        for i in range(len(nums)):
            groups[i % k].append(nums[i])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k

        for i in range(k):
            group_list = groups[i]
            for num in group_list:
                freq[i][num] += 1
            min_size[i] = len(group_list)

        MAX_MASK = 1 << 10
        dp = [inf] * MAX_MASK
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_MASK
            min_dp = min(dp)
            for j in range(MAX_MASK):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]