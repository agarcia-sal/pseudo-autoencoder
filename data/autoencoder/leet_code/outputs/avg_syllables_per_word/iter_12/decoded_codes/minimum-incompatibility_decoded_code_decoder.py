from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        counts = Counter(nums).values()
        if any(count > k for count in counts):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        # Precompute incompatibility for all valid subsets of size subset_size with unique elements
        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i)) != 0]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(full_mask + 1):
            bit_count = bin(mask).count('1')
            if bit_count % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                # If subset_mask is contained in mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    candidate = dp[prev_mask] + subset_incompatibility[subset_mask]
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        return -1 if dp[full_mask] == INF else dp[full_mask]