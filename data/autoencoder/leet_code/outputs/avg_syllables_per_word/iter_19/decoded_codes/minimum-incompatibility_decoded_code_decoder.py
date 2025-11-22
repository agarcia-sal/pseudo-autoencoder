from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        counter = Counter(nums)
        if any(count > k for count in counter.values()):
            return -1

        subset_incompatibility = {}
        # Precompute all valid subsets with size subset_size and unique elements
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
            if dp[mask] == inf:
                continue
            remaining = ((1 << n) - 1) ^ mask
            # Iterate over all subsets of remaining with size subset_size and unique elements
            # to avoid redundant checks, intersect keys with remaining subsets only
            # But here we rely on subset_incompatibility keys all subsets of size subset_size
            for subset_mask in subset_incompatibility:
                if (subset_mask & mask) == 0 and (subset_mask & remaining) == subset_mask:
                    new_mask = mask | subset_mask
                    dp[new_mask] = min(dp[new_mask], dp[mask] + subset_incompatibility[subset_mask])

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != inf else -1