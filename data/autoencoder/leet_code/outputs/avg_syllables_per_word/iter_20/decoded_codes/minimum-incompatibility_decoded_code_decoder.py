from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        freq = Counter(nums)
        if any(count > k for count in freq.values()):
            return -1

        subset_incompatibility = {}

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        # Use bitmask from 0 to 2^n - 1
        # For efficiency, collect indexes and elements once per mask, checking uniqueness with a set
        for mask in range(1 << n):
            # Count set bits quickly by builtin function
            if bin(mask).count('1') == subset_size:
                elements = []
                seen = set()
                valid = True
                m = mask
                i = 0
                while m:
                    if m & 1:
                        val = nums[i]
                        if val in seen:
                            valid = False
                            break
                        seen.add(val)
                        elements.append(val)
                    m >>= 1
                    i += 1
                if valid:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        # dp[mask]: minimum total incompatibility for the subset of elements represented by mask
        # We want dp[(1 << n) - 1] as final answer
        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            count_ones = bin(mask).count('1')
            if count_ones % subset_size != 0:
                continue
            # try to form next group subset_mask fully contained in mask
            # to update dp[mask], check subsets subset_mask contained in mask that are valid groups
            for subset_mask, incompat in subset_incompatibility.items():
                # subset_mask should be subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    if dp[prev_mask] + incompat < dp[mask]:
                        dp[mask] = dp[prev_mask] + incompat

        final_mask = (1 << n) - 1
        return dp[final_mask] if dp[final_mask] != inf else -1