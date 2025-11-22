from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        # If any number appears more times than k, it's impossible to form k subsets without duplicates
        freq = Counter(nums)
        if any(count > k for count in freq.values()):
            return -1

        subset_incompatibility = {}
        full_mask = (1 << n) - 1

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        for mask in range(full_mask + 1):
            if bin(mask).count('1') == subset_size:
                elements = []
                for i in range(n):
                    if mask & (1 << i):
                        elements.append(nums[i])
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        # Build up dp for all masks representing combinations of subsets
        for mask in range(full_mask + 1):
            # Only proceed if the number of elements selected is multiple of subset_size
            if (bin(mask).count('1') % subset_size) != 0:
                continue

            for subset_mask, incompat in subset_incompatibility.items():
                # Check if subset_mask is a subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != float('inf'):
                        candidate = dp[prev_mask] + incompat
                        if candidate < dp[mask]:
                            dp[mask] = candidate

        return dp[full_mask] if dp[full_mask] != float('inf') else -1