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

        MAX_XOR = 1 << 10
        dp = [inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_XOR
            min_dp = min(dp)
            for j in range(MAX_XOR):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    new_dp[j] = min(new_dp[j], dp[j ^ num] + min_size[i] - count)
            dp = new_dp

        return dp[0]