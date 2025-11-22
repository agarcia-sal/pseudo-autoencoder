from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        freq = Counter(nums)
        if any(count > k for count in freq.values()):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = []
                # Gather elements corresponding to bits set in mask
                for index in range(n):
                    if (mask >> index) & 1:
                        elements.append(nums[index])
                # Check uniqueness
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (full_mask + 1)
        dp[0] = 0

        # State DP over subsets of nums
        for mask in range(full_mask + 1):
            if dp[mask] == inf:
                continue
            bit_count = bin(mask).count('1')
            # Can only add subsets to full subsets that align with subset_size
            if bit_count % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                # subset_mask must be disjoint from mask
                if (mask & subset_mask) == 0:
                    next_mask = mask | subset_mask
                    if dp[next_mask] > dp[mask] + incompatibility:
                        dp[next_mask] = dp[mask] + incompatibility

        return dp[full_mask] if dp[full_mask] != inf else -1