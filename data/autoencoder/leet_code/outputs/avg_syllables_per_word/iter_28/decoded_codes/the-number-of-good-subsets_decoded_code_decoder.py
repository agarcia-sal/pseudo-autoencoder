from collections import Counter
from typing import List

MOD = 10 ** 9 + 7

# Predefined mapping of nums to their prime factor masks using primes:
# The primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 indexed 0..9
# The mask stores which primes are present in the prime factorization of the num,
# but only if the num has no repeated prime factors (square-free).
# This mask is used as a bitmask of length 10.
prime_factors = {
    2: [2],
    3: [3],
    5: [5],
    6: [2, 3],
    7: [7],
    10: [2, 5],
    11: [11],
    13: [13],
    14: [2, 7],
    15: [3, 5],
    17: [17],
    19: [19],
    21: [3, 7],
    22: [2, 11],
    23: [23],
    26: [2, 13],
    29: [29],
    30: [2, 3, 5],
}

# Since prime_factors keys and primes values are all <= 30 (max),
# map primes to their bit positions for mask calculation.
prime_to_bit = {
    2: 0,
    3: 1,
    5: 2,
    7: 3,
    11: 4,
    13: 5,
    17: 6,
    19: 7,
    23: 8,
    29: 9,
}

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        if 1 in count:
            dp[0] = pow(2, count[1], MOD)

        for num, freq in count.items():
            if num == 1:
                continue

            if num not in prime_factors:
                # Either has squared prime factors (not square-free), or >30.
                continue

            factors = prime_factors[num]
            mask = 0
            for prime in factors:
                bit = prime_to_bit[prime]
                # If bit already set, repeated prime factor -> skip
                # (Though predefined prime_factors already exclude these)
                if (mask & (1 << bit)) != 0:
                    mask = 0
                    break
                mask |= (1 << bit)
            if mask == 0:
                continue

            # Iterate dp backwards to avoid using updated states within same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % MOD

        return sum(dp[1:]) % MOD