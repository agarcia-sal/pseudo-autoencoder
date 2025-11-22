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
        full_mask = (1 << n) - 1

        # Precompute all subsets of size subset_size with unique elements and their incompatibility
        for mask in range(full_mask + 1):
            # Count number of bits set in mask
            bit_count = bin(mask).count('1')
            if bit_count == subset_size:
                elements = []
                seen = set()
                valid = True
                for i in range(n):
                    if (mask & (1 << i)) != 0:
                        val = nums[i]
                        if val in seen:
                            valid = False
                            break
                        seen.add(val)
                        elements.append(val)
                if valid:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            if bit_count % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                # Check if subset_mask is a subset of mask
                if (mask & subset_mask) == subset_mask:
                    candidate = dp[mask ^ subset_mask] + subset_incompatibility[subset_mask]
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        return dp[full_mask] if dp[full_mask] != inf else -1