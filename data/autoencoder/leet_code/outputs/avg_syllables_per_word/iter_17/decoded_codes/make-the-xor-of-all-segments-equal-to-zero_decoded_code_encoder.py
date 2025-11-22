from collections import defaultdict, Counter
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        n = len(nums)
        for i in range(n):
            groups[i % k].append(nums[i])

        freq = [Counter() for _ in range(k)]
        min_size = [0] * k
        for i in range(k):
            freq[i].update(groups[i])
            min_size[i] = len(groups[i])

        MAX_XOR = 1 << 10  # 2 ** 10 == 1024
        dp = [inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_XOR
            min_dp = min(dp)
            group_len = min_size[i]
            for x in range(MAX_XOR):
                # Initialize with min_dp + all elements of current group changed
                new_dp[x] = min_dp + group_len
                for num, count in freq[i].items():
                    candidate = dp[x ^ num] + group_len - count
                    if candidate < new_dp[x]:
                        new_dp[x] = candidate
            dp = new_dp

        return dp[0]