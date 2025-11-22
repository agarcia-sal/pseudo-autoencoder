from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        if any(v > k for v in count.values()):
            return -1

        full_mask = (1 << n) - 1
        subset_incompatibility = {}

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
            if dp[mask] == float('inf'):
                continue
            if bin(mask).count('1') % subset_size != 0:
                continue
            remain = full_mask ^ mask
            sub = remain
            while sub:
                if sub in subset_incompatibility:
                    new_mask = mask | sub
                    val = dp[mask] + subset_incompatibility[sub]
                    if val < dp[new_mask]:
                        dp[new_mask] = val
                sub = (sub - 1) & remain

        return dp[full_mask] if dp[full_mask] != float('inf') else -1