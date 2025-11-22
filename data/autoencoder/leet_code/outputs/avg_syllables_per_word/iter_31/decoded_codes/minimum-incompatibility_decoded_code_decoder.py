from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        counts = Counter(nums)
        if any(v > k for v in counts.values()):
            return -1

        subset_incompatibility = {}
        # Precompute incompatibility of all subsets of size subset_size with unique elements
        for mask in range(1 << n):
            if bin(mask).count('1') != subset_size:
                continue
            elements = []
            for i in range(n):
                if (mask >> i) & 1:
                    elements.append(nums[i])
            if len(set(elements)) == subset_size:
                incompatibility = max(elements) - min(elements)
                subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            bits_count = bin(mask).count('1')
            if bits_count % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (subset_mask & mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    candidate = dp[prev_mask] + incompatibility
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        full_mask = (1 << n) - 1
        return dp[full_mask] if dp[full_mask] != inf else -1