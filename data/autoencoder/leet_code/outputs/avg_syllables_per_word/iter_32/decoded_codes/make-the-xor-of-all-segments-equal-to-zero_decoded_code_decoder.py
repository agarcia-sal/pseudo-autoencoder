from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        groups = defaultdict(list)
        n = len(nums)
        for i in range(n):
            groups[i % k].append(nums[i])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k

        for i in range(k):
            for num in groups[i]:
                freq[i][num] += 1
            min_size[i] = len(groups[i])

        MAX_XOR = 1 << 10  # 2^10

        dp = [inf] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [inf] * MAX_XOR
            min_dp = min(dp)
            for j in range(MAX_XOR):
                # If we do not match any existing pattern, we replace all elements in group i
                new_dp[j] = min_dp + min_size[i]

                # Try to align with each number in freq[i]
                for num, count in freq[i].items():
                    # Reset positions in group i to num, the cost is min_size[i] - count
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]