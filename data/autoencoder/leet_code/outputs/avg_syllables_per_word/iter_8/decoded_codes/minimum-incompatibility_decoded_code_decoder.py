class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        from collections import Counter
        freq = Counter(nums)
        for count in freq.values():
            if count > k:
                return -1

        subset_incompatibility = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = []
                seen = set()
                valid = True
                for i in range(n):
                    if (mask >> i) & 1:
                        val = nums[i]
                        if val in seen:
                            valid = False
                            break
                        seen.add(val)
                        elements.append(val)
                if valid:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if bin(mask).count('1') % subset_size != 0:
                continue
            for subset_mask in subset_incompatibility:
                if (subset_mask & mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] != INF:
                        dp[mask] = min(dp[mask], dp[prev_mask] + subset_incompatibility[subset_mask])

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != INF else -1