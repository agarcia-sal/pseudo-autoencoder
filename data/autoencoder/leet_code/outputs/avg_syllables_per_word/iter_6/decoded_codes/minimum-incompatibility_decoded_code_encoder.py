from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        subset_incompatibility = {}
        # Precompute all valid subsets and their incompatibility
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = []
                seen = set()
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        if nums[i] in seen:
                            valid = False
                            break
                        seen.add(nums[i])
                        elements.append(nums[i])
                if valid:
                    subset_incompatibility[mask] = max(elements) - min(elements)

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == float('inf') or bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (mask & subset_mask) == 0:
                    new_mask = mask | subset_mask
                    if dp[new_mask] > dp[mask] + incompatibility:
                        dp[new_mask] = dp[mask] + incompatibility

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1