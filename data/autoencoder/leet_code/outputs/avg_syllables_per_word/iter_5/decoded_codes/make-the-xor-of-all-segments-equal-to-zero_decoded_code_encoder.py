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

        size = 1 << 10
        dp = [inf] * size
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * size
            min_dp = min(dp)
            for j in range(size):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]