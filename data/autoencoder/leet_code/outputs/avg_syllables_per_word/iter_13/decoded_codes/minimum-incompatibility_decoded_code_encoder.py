from typing import List
from collections import Counter
import math

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        def count_occurrences_of_elements(input_list: List[int]) -> dict[int, int]:
            return Counter(input_list)

        element_counts = count_occurrences_of_elements(nums)
        if any(count > k for count in element_counts.values()):
            return -1

        def generate_valid_subsets() -> dict[int, int]:
            subset_incompatibility = {}
            # Iterate over all subsets of size subset_size
            # Use bitmask from 0 to 2^n - 1
            limit = 1 << n
            for mask in range(limit):
                if bin(mask).count('1') == subset_size:
                    elements = []
                    # Extract elements corresponding to bits set in mask
                    bit = 0
                    m = mask
                    while m:
                        if m & 1:
                            elements.append(nums[bit])
                        m >>= 1
                        bit += 1
                    # If all elements unique
                    if len(set(elements)) == subset_size:
                        incompatibility_value = max(elements) - min(elements)
                        subset_incompatibility[mask] = incompatibility_value
            return subset_incompatibility

        subset_incompatibility = generate_valid_subsets()

        dp = [math.inf] * (1 << n)
        dp[0] = 0

        limit = 1 << n
        for mask in range(limit):
            bit_count = bin(mask).count('1')
            if bit_count % subset_size != 0:
                continue
            current_value = dp[mask]
            if current_value == math.inf:
                continue
            # Try to add subsets (subset_mask) to current mask
            for subset_mask, incompat_val in subset_incompatibility.items():
                # subset_mask must be disjoint with mask (subset_mask & mask == 0)
                if (mask & subset_mask) == 0:
                    next_mask = mask | subset_mask
                    next_value = current_value + incompat_val
                    if next_value < dp[next_mask]:
                        dp[next_mask] = next_value

        full_mask = (1 << n) - 1
        return dp[full_mask] if dp[full_mask] != math.inf else -1