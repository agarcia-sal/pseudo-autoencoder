from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        subset_incompatibility = {}
        total_mask = 1 << n

        # Precompute incompatibility for all valid subsets of size subset_size
        for mask in range(total_mask):
            if bin(mask).count('1') == subset_size:
                elements = []
                for i in range(n):
                    if (mask & (1 << i)) != 0:
                        elements.append(nums[i])
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * total_mask
        dp[0] = 0

        for mask in range(total_mask):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                # Check if subset_mask is a subset of mask
                if (mask & subset_mask) == subset_mask:
                    remaining = mask ^ subset_mask
                    if dp[remaining] != inf:
                        dp[mask] = min(dp[mask], dp[remaining] + subset_incompatibility[subset_mask])

        return dp[total_mask - 1] if dp[total_mask - 1] != inf else -1