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
        # Precompute incompatibility for all subsets of size subset_size with unique elements
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = []
                seen = set()
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        val = nums[i]
                        if val in seen:
                            valid = False
                            break
                        seen.add(val)
                        elements.append(val)
                if not valid:
                    continue
                incompatibility = max(elements) - min(elements)
                subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != inf:
                        dp[mask] = min(dp[mask], dp[prev_mask] + incompatibility)

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != inf else -1