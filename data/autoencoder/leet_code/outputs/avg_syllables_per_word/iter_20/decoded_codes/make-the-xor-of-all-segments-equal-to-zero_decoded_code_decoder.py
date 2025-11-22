from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[i % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k

        for i in range(k):
            group = groups[i]
            for num in group:
                freq[i][num] += 1
            min_size[i] = len(group)

        MAX_XOR = 1 << 10  # 2^10

        dp = [inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_XOR
            min_dp = min(dp)
            group_size = min_size[i]
            freq_map = freq[i]

            for j in range(MAX_XOR):
                new_dp[j] = min_dp + group_size  # Change all in group

                for number, count in freq_map.items():
                    candidate = dp[j ^ number] + group_size - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate

            dp = new_dp

        return dp[0]