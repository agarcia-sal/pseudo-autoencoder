from collections import defaultdict
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        groups = defaultdict(list)
        for index, num in enumerate(nums):
            groups[index % k].append(num)

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [float('inf')] * k
        for index in range(k):
            for num in groups[index]:
                freq[index][num] += 1
            min_size[index] = len(groups[index])

        MAX_XOR = 1 << 10
        dp = [float('inf')] * MAX_XOR
        dp[0] = 0

        for index in range(k):
            new_dp = [float('inf')] * MAX_XOR
            min_dp = min(dp)
            for j in range(MAX_XOR):
                # Change all group elements to arbitrary values: cost min_size[index]
                new_dp[j] = min_dp + min_size[index]
                for num, count in freq[index].items():
                    candidate = dp[j ^ num] + min_size[index] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]