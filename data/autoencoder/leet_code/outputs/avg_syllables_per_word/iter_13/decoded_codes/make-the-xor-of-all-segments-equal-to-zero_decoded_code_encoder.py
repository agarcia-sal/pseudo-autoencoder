from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        groups = defaultdict(list)
        for idx, num in enumerate(nums):
            groups[idx % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k
        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        dp = [inf] * 1024
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * 1024
            min_dp = min(dp)
            for j in range(1024):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    candidate_value = dp[j ^ num] + min_size[i] - count
                    if candidate_value < new_dp[j]:
                        new_dp[j] = candidate_value
            dp = new_dp

        return dp[0]