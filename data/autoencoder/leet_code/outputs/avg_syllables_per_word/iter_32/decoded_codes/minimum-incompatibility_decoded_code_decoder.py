from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        # If any element appears more than k times, no valid partition possible
        counts = Counter(nums)
        if any(count > k for count in counts.values()):
            return -1

        subset_incompatibility = {}

        # Precompute incompatibility for all subsets of size subset_size with unique elements
        # mask represents subset of nums by bitmask of length n
        # We optimize by generating combinations rather than iterating all 2^n masks
        # but we will keep to pseudocode logic for strict translation.

        # To generate all subsets of size subset_size quickly with unique elements, 
        # we proceed with bitmasking as stated, checking uniqueness.

        # Since n <= 16 (typical constraint for problems with subset dp like this),
        # enumerating all subsets is acceptable.
        # note: For large n, this approach is not feasible, but we follow given pseudocode.

        for mask in range(1 << n):
            # Check if bit count == subset_size
            if bin(mask).count('1') == subset_size:
                elements = []
                unique_check = set()
                valid = True
                for i in range(n):
                    if (mask >> i) & 1:
                        elem = nums[i]
                        if elem in unique_check:
                            valid = False
                            break
                        unique_check.add(elem)
                        elements.append(elem)
                if valid:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * (1 << n)
        dp[0] = 0

        # For each mask of chosen elements, if count of ones is multiple of subset_size,
        # try partitioning into subsets already computed.
        for mask in range(1 << n):
            # Only consider masks with number of set bits divisible by subset_size
            if (bin(mask).count('1') % subset_size) != 0:
                continue
            if dp[mask] == inf:
                continue
            # Try to extend mask by subsets in subset_incompatibility that don't overlap mask
            # Pseudocode says: if (mask & subset_mask) == subset_mask, set dp[mask] based on dp[mask - subset_mask].
            # But this means subset_mask is a subset of mask.
            # So we must try subsets subset_mask which are subsets of mask.
            # However, the pseudocode iterates over all subset_mask and checks if (mask & subset_mask) == subset_mask.
            # We'll follow that exactly for correctness.

            # Optimized approach: For each subset_mask that is subset of mask
            # dp[mask] can be updated using dp[mask - subset_mask] + incompatibility

        # Actually, the pseudocode logic has a subtle difference:
        # The pseudocode loops mask from 0 to 2^n - 1
        # For each subset_mask in subset_incompatibility:
        # if (mask & subset_mask) == subset_mask (subset_mask is subset of mask)
        # dp[mask] = min(dp[mask], dp[mask - subset_mask] + subset_incompatibility[subset_mask])

        # So we implement that exactly.

        for mask in range(1 << n):
            # Only consider masks with set bits count divisible by subset_size AND dp[mask]!=inf
            if (bin(mask).count('1') % subset_size) != 0 or dp[mask] == inf:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                # Check if subset_mask is subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask  # bits in mask but not in subset_mask
                    new_val = dp[prev_mask] + incompatibility
                    if new_val < dp[mask]:
                        dp[mask] = new_val

        full_mask = (1 << n) - 1
        return dp[full_mask] if dp[full_mask] != inf else -1