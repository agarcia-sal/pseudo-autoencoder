from collections import Counter
from typing import List

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        # Prime factors sets without square factors for numbers 2..30:
        # Each number maps to a bitmask representing the primes dividing it
        # Primes considered: 2,3,5,7,11,13,17,19,23,29 (ten primes)
        prime_index = {2:0,3:1,5:2,7:3,11:4,13:5,17:6,19:7,23:8,29:9}
        prime_factors = {
            2: {2},
            3: {3},
            5: {5},
            6: {2,3},
            7: {7},
            10: {2,5},
            11: {11},
            13: {13},
            14: {2,7},
            15: {3,5},
            17: {17},
            19: {19},
            21: {3,7},
            22: {2,11},
            23: {23},
            26: {2,13},
            29: {29},
            30: {2,3,5}
        }

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle '1's separately: can be in any subset or not, doubling count for each '1'
        pow2_ones = pow(2, count.get(1, 0), mod)
        dp[0] = (dp[0] * pow2_ones) % mod

        # For each unique number excluding 1
        for num, freq in count.items():
            if num == 1:
                continue
            if num not in prime_factors:
                continue

            # Calculate mask for the prime factors
            mask = 0
            for prime in prime_factors[num]:
                mask |= 1 << prime_index[prime]

            # Update dp from high to low to avoid double counting
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % mod

        return sum(dp[1:]) % mod