from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        counts = Counter(nums).values()
        if any(count > k for count in counts):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        # Precompute incompatibility for all valid subsets of size subset_size without duplicates
        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = []
                for i in range(n):
                    if (mask & (1 << i)) != 0:
                        elements.append(nums[i])
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (full_mask + 1)
        dp[0] = 0

        for mask in range(full_mask + 1):
            bit_count = bin(mask).count('1')
            if bit_count % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                if (mask & subset_mask) == subset_mask:
                    dp[mask] = min(dp[mask], dp[mask ^ subset_mask] + subset_incompatibility[subset_mask])

        return dp[full_mask] if dp[full_mask] != inf else -1