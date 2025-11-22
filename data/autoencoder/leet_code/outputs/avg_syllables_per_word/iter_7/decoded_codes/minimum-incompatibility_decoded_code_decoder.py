from typing import List
from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i))]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (full_mask + 1)
        dp[0] = 0

        for mask in range(full_mask + 1):
            if (bin(mask).count('1') % subset_size) != 0:
                continue
            for subset_mask in subset_incompatibility:
                if (subset_mask & mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    dp[mask] = min(dp[mask], dp[prev_mask] + subset_incompatibility[subset_mask])

        return -1 if dp[full_mask] == inf else dp[full_mask]