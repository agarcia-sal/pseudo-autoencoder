from typing import List
from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        limit = 1 << n
        subset_incompatibility = {}
        for mask in range(limit):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if mask & (1 << i)]
                if len(set(elements)) == subset_size:
                    subset_incompatibility[mask] = max(elements) - min(elements)

        dp = [float('inf')] * limit
        dp[0] = 0

        for mask in range(limit):
            if dp[mask] == float('inf') or (bin(mask).count('1') % subset_size != 0):
                continue
            remain = ((limit - 1) ^ mask)
            sub = remain
            while sub:
                if sub in subset_incompatibility:
                    new_mask = mask | sub
                    dp[new_mask] = min(dp[new_mask], dp[mask] + subset_incompatibility[sub])
                sub = (sub - 1) & remain

        return dp[limit - 1] if dp[limit - 1] != float('inf') else -1