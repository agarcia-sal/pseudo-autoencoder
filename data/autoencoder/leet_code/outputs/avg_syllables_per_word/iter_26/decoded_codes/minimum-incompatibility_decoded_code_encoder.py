from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        if any(count > k for count in Counter(nums).values()):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i)) != 0]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (full_mask + 1)
        dp[0] = 0

        for mask in range(full_mask + 1):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != inf:
                        dp[mask] = min(dp[mask], dp[prev_mask] + incompatibility)

        return dp[full_mask] if dp[full_mask] != inf else -1