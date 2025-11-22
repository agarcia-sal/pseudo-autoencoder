from typing import List
from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        count = Counter(nums)
        # If any number appears more than k times, return -1 immediately
        if any(v > k for v in count.values()):
            return -1

        subset_incompatibility = {}
        # Precompute all subsets of size subset_size and their incompatibility if valid
        # Using bitmask from 0 to 2^n - 1
        # To optimize, gather indices for nums so that we can avoid repeated scans
        # However, given constraints, direct bit manipulation is feasible

        def bit_count(x: int) -> int:
            return bin(x).count('1')

        # For quick check if elements are unique, we can check length(set(elements)) == subset_size
        # Precompute for all masks with exactly subset_size bits set
        for mask in range(1 << n):
            if bit_count(mask) == subset_size:
                elements = []
                seen = set()
                valid = True
                # Collect elements and check uniqueness
                bit = 0
                temp = mask
                while temp:
                    if temp & 1:
                        val = nums[bit]
                        if val in seen:
                            valid = False
                            break
                        seen.add(val)
                        elements.append(val)
                    temp >>= 1
                    bit += 1
                if valid:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        # For every mask, only consider masks with bits count divisible by subset_size
        # For each mask, try each subset_mask in subset_incompatibility that is subset of mask
        # Update dp[mask] = min(dp[mask], dp[mask ^ subset_mask] + incompatibility)
        # To optimize subset checks, we iterate over mask, then subset_incompatibility keys;
        # Because n can be up to 16 (reasonable for 2^n), this is acceptable.

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            # Current mask has bit count divisible by subset_size?
            if (bit_count(mask) % subset_size) != 0:
                continue
            # We want to pick next subset of subset_size elements disjoint with mask
            # Actually, from pseudocode, it checks subset_mask is subset of mask
            # But dp[mask] is computed from dp[mask ^ subset_mask], so mask should be superset of subset_mask
            # Here, since dp is built forward (from smaller to bigger masks)
            # Actually correcting logic: we want to build dp[mask | subset_mask] from dp[mask]:
            # Because dp[mask | subset_mask] = min(dp[mask | subset_mask], dp[mask] + incompatibility(subset_mask))
            # So the pseudocode is backward; to optimize, we do forwards.

        # So change approach to forward dp:
        # For mask from 0 to 2^n -1:
        # If dp[mask] is not INF and popcount(mask) divisible by subset_size:
        # For each subset_mask in subset_incompatibility:
        #     If mask & subset_mask == 0 (disjoint sets)
        #         next_mask = mask | subset_mask
        #         dp[next_mask] = min(dp[next_mask], dp[mask] + subset_incompatibility[subset_mask])

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            if (bit_count(mask) % subset_size) != 0:
                continue
            for subset_mask, incompatibility in subset_incompatibility.items():
                if (mask & subset_mask) == 0:
                    next_mask = mask | subset_mask
                    if dp[next_mask] > dp[mask] + incompatibility:
                        dp[next_mask] = dp[mask] + incompatibility

        res = dp[(1 << n) - 1]
        return -1 if res == INF else res