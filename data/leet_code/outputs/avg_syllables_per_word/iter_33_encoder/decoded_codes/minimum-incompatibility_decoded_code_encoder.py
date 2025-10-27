from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        freq = Counter(nums)
        if any(count > k for count in freq.values()):
            return -1

        subset_incompatibility = {}
        total_masks = 1 << n

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        for mask in range(total_masks):
            # Count bits set in mask
            if bin(mask).count('1') == subset_size:
                elements = []
                # Collect elements corresponding to set bits in mask
                for i in range(n):
                    if mask & (1 << i):
                        elements.append(nums[i])
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * total_masks
        dp[0] = 0

        # Iterate over all masks with bit count divisible by subset_size
        for mask in range(total_masks):
            if dp[mask] == inf:
                continue
            bit_count = bin(mask).count('1')
            if bit_count % subset_size != 0:
                continue
            # Try adding a valid subset to current mask
            for subset_mask, incompatibility in subset_incompatibility.items():
                # Check if subset_mask can be added without overlap
                if (mask & subset_mask) == 0:
                    new_mask = mask | subset_mask
                    if dp[new_mask] > dp[mask] + incompatibility:
                        dp[new_mask] = dp[mask] + incompatibility

        full_mask = total_masks - 1
        return dp[full_mask] if dp[full_mask] != inf else -1