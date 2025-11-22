from typing import List, Dict
from collections import defaultdict
import math

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # Group elements by their index mod k
        groups: Dict[int, List[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            groups[i % k].append(num)

        freq: List[Dict[int, int]] = [defaultdict(int) for _ in range(k)]
        min_size: List[int] = [math.inf] * k

        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        MAX_XOR = 1 << 10  # 2^10 = 1024

        dp = [math.inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [math.inf] * MAX_XOR
            min_dp = min(dp)
            for j in range(MAX_XOR):
                # If we change all elements in group i
                new_dp[j] = min_dp + min_size[i]

                for num, count in freq[i].items():
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]