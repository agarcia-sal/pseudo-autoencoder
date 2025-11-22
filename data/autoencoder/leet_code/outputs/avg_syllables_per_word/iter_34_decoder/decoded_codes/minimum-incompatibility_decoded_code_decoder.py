from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        if any(c > k for c in count.values()):
            return -1

        subset_incompatibility = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i)) != 0]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility.keys():
                if (mask & subset_mask) == subset_mask:
                    candidate = dp[mask ^ subset_mask] + subset_incompatibility[subset_mask]
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        full_mask = (1 << n) - 1
        return dp[full_mask] if dp[full_mask] != inf else -1