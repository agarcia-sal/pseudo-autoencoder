from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[i % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [0] * k

        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        MAX_XOR = 1 << 10  # 2**10
        dp = [inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_XOR
            min_dp = min(dp)
            for mask in range(MAX_XOR):
                new_dp[mask] = min_dp + min_size[i]
                for num_key, count in freq[i].items():
                    candidate = dp[mask ^ num_key] + min_size[i] - count
                    if candidate < new_dp[mask]:
                        new_dp[mask] = candidate
            dp = new_dp

        return dp[0]