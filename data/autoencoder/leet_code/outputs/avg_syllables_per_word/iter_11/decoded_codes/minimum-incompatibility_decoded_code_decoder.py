from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        if any(count > k for count in Counter(nums).values()):
            return -1

        subset_incompatibility = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = [nums[i] for i in range(n) if (mask & (1 << i)) != 0]
                if len(set(elements)) == subset_size:
                    subset_incompatibility[mask] = max(elements) - min(elements)

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            count_ones = bin(mask).count('1')
            if count_ones % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                if (mask & subset_mask) == subset_mask:
                    dp[mask] = min(dp[mask], dp[mask ^ subset_mask] + subset_incompatibility[subset_mask])

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1