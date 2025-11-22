from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        subset_incompatibility = {}
        # Precompute incompatibility for all valid subsets
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i))]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (mask & subset_mask) == 0:
                    new_mask = mask | subset_mask
                    dp[new_mask] = min(dp[new_mask], dp[mask] + incompatibility)

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != INF else -1