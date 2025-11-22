from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k
        count = Counter(nums)
        # If any number appears more than k times, can't partition without duplicates in a subset
        if any(c > k for c in count.values()):
            return -1

        subset_incompatibility = {}
        # Precompute incompatibilities for all valid subsets of size subset_size
        # Use bitmask from 0 to 2^n - 1
        # For efficiency, generate all subsets of size subset_size using bitmasks
        # and check if their elements have duplicates

        # There are up to C(n, subset_size) subsets, which may be large,
        # but since constraints are not given, we implement faithfully

        # To speed up counting bits, we can use bin(mask).count('1')
        for mask in range(1 << n):
            if bin(mask).count('1') == subset_size:
                elements = []
                for i in range(n):
                    if (mask & (1 << i)) != 0:
                        elements.append(nums[i])
                # Check if all elements unique in subset
                if len(set(elements)) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0

        # Iterate over all masks with number of selected elements multiple of subset_size
        for mask in range(1 << n):
            if dp[mask] == inf:
                # No need to proceed if current dp state is inf
                continue
            if (bin(mask).count('1') % subset_size) != 0:
                continue
            # Try to add a valid subset that is subset_mask from subset_incompatibility
            # which is a subset of elements not selected in 'mask' yet
            # Wait, pseudocode says: if mask & subset_mask == subset_mask:
            # but that would mean subset_mask is subset of mask.
            # However, in DP formulation, mask represents selected elements.
            # The logic: to build dp[mask], we consider subsets of mask.
            # Here the pseudocode is building up dp[mask] from dp[mask ^ subset_mask].
            # So we should consider subset_masks that are subsets of mask.
            # So for every subset_mask in subset_incompatibility keys:
            # if subset_mask is subset of mask:
            #   dp[mask] = min(dp[mask], dp[mask ^ subset_mask] + subset_incompatibility[subset_mask])

            # So we only update dp[mask] if mask contains subset_mask ?

            # But current implementation loops mask from 0..2^n-1
            # and update dp[mask] based on dp[mask ^ subset_mask].

            # So for current mask, try removing subset_mask subsets and get better dp

            # We'll implement as pseudocode given.

            for subset_mask in subset_incompatibility:
                # Check if subset_mask is a subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev = mask ^ subset_mask
                    if dp[prev] != inf:
                        dp[mask] = min(dp[mask], dp[prev] + subset_incompatibility[subset_mask])

        full_mask = (1 << n) - 1
        return -1 if dp[full_mask] == inf else dp[full_mask]