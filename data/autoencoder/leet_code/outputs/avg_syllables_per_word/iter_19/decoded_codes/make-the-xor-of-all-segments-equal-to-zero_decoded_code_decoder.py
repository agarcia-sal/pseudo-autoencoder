from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        for idx, num in enumerate(nums):
            groups[idx % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k
        for pos in range(k):
            for num in groups[pos]:
                freq[pos][num] += 1
            min_size[pos] = len(groups[pos])

        MAX_MASK = 1 << 10  # 2^10 = 1024
        dp = [inf] * MAX_MASK
        dp[0] = 0

        for pos in range(k):
            new_dp = [inf] * MAX_MASK
            min_dp = min(dp)
            size = min_size[pos]
            f = freq[pos]
            for mask in range(MAX_MASK):
                # Change all in group to arbitrary (min_dp + size)
                new_dp[mask] = min_dp + size
                # Try to keep some common numbers to reduce changes
                for num, count in f.items():
                    val = dp[mask ^ num] + size - count
                    if val < new_dp[mask]:
                        new_dp[mask] = val
            dp = new_dp

        return dp[0]