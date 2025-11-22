from collections import Counter
from math import inf

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        subset_size = n // k

        count_map = Counter(nums)
        for c in count_map.values():
            if c > k:
                return -1

        subset_incompatibility = {}

        limit = 1 << n  # 2 ** n
        for mask in range(limit):
            # Count bits set in mask
            bit_count = 0
            for bit_pos in range(n):
                if (mask >> bit_pos) & 1:
                    bit_count += 1

            if bit_count == subset_size:
                elements = []
                for idx in range(n):
                    if (mask >> idx) & 1:
                        elements.append(nums[idx])

                unique_check = set(elements)
                if len(unique_check) == subset_size:
                    incompatibility = max(elements) - min(elements)
                    subset_incompatibility[mask] = incompatibility

        dp = [inf] * limit
        dp[0] = 0

        for mask in range(limit):
            # Count bits set in mask
            current_bit_count = 0
            for bit_pos in range(n):
                if (mask >> bit_pos) & 1:
                    current_bit_count += 1

            if current_bit_count % subset_size != 0:
                continue

            for subset_mask, incompatibility in subset_incompatibility.items():
                # Check if subset_mask is a subset of mask
                if (mask & subset_mask) == subset_mask:
                    prev_mask = mask ^ subset_mask
                    possible_value = dp[prev_mask] + incompatibility
                    if possible_value < dp[mask]:
                        dp[mask] = possible_value

        full_mask = limit - 1
        return -1 if dp[full_mask] == inf else dp[full_mask]