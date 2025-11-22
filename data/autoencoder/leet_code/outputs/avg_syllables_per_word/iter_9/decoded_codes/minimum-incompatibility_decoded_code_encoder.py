from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        if any(count > k for count in Counter(nums).values()):
            return -1

        subset_incompatibility = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if mask & (1 << i)]
                if len(set(elements)) == subset_size:
                    subset_incompatibility[mask] = max(elements) - min(elements)

        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask, incompat in subset_incompatibility.items():
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != inf:
                        dp[mask] = min(dp[mask], dp[prev_mask] + incompat)

        return -1 if dp[(1 << n) - 1] == inf else dp[(1 << n) - 1]