from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[i % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k

        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        limit = 1 << 10  # 2^10
        dp = [inf] * limit
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * limit
            min_dp = min(dp)
            for j in range(limit):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    val = dp[j ^ num] + min_size[i] - count
                    if val < new_dp[j]:
                        new_dp[j] = val
            dp = new_dp

        return dp[0]