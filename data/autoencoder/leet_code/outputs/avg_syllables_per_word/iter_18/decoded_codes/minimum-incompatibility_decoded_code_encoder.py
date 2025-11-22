from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        # If any element appears more than k times, no valid partition is possible
        if any(count > k for count in Counter(nums).values()):
            return -1

        subset_incompatibility = {}

        # Precompute incompatibility for all valid subsets of size subset_size without duplicates
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i)) != 0]
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            # Process dp states only if number of chosen elements is multiple of subset_size
            if bin(mask).count('1') % subset_size != 0:
                continue

            for subset_mask, incompatibility in subset_incompatibility.items():
                # Check if subset_mask is subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != float('inf'):
                        dp[mask] = min(dp[mask], dp[prev_mask] + incompatibility)

        full_mask = (1 << n) - 1
        return dp[full_mask] if dp[full_mask] != float('inf') else -1