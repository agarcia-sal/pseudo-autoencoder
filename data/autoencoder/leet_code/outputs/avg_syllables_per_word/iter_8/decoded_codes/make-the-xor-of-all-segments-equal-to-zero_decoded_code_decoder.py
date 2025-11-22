from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        for i in range(len(nums)):
            groups[i % k].append(nums[i])
        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k
        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])
        dp = [inf] * (1 << 10)
        dp[0] = 0
        for i in range(k):
            new_dp = [inf] * (1 << 10)
            min_dp = min(dp)
            for j in range(1 << 10):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    x = j ^ num
                    cost = dp[x] + min_size[i] - count
                    if cost < new_dp[j]:
                        new_dp[j] = cost
            dp = new_dp
        return dp[0]