from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        counts = Counter(nums)
        if any(c > k for c in counts.values()):
            return -1

        subset_incompatibility = {}
        total_masks = 1 << n

        for mask in range(total_masks):
            if bin(mask).count('1') == subset_size:
                elements = []
                for i in range(n):
                    if (mask & (1 << i)) != 0:
                        elements.append(nums[i])
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [float('inf')] * total_masks
        dp[0] = 0

        for mask in range(total_masks):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                if (mask & subset_mask) == subset_mask:
                    dp[mask] = min(dp[mask], dp[mask ^ subset_mask] + subset_incompatibility[subset_mask])

        return -1 if dp[total_masks - 1] == float('inf') else dp[total_masks - 1]