from collections import Counter
from typing import List

MOD = 10**9 + 7

# Predefined prime factors for numbers 2 to 30 that do not contain square factors
# Each prime is represented by an index from 0 to 9 corresponding to primes:
# 2,3,5,7,11,13,17,19,23,29
# We select numbers that are square-free and have their prime factor sets with no duplicates.
prime_factors = {
    2: [0],       # prime index for 2
    3: [1],       # prime index for 3
    5: [2],       # prime index for 5
    6: [0, 1],    # 2*3
    7: [3],       # prime index for 7
    10: [0, 2],   # 2*5
    11: [4],      # prime index for 11
    13: [5],      # prime index for 13
    14: [0, 3],   # 2*7
    15: [1, 2],   # 3*5
    17: [6],      # prime index for 17
    19: [7],      # prime index for 19
    21: [1, 3],   # 3*7
    22: [0, 4],   # 2*11
    23: [8],      # prime index for 23
    26: [0, 5],   # 2*13
    29: [9],      # prime index for 29
    30: [0, 1, 2],# 2*3*5
}

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        # dp mask from 0..(1 << 10) - 1, dp[m] counts subsets represented by used prime bits m
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle 1 separately: 1 can be chosen any number of times without adding prime factors
        if 1 in count:
            dp[0] = pow(2, count[1], MOD)

        # Iterate over nums keys excluding 1
        for num in count:
            if num == 1:
                continue
            if num not in prime_factors:
                continue
            factors = prime_factors[num]
            mask = 0
            for prime in factors:
                mask |= 1 << prime

            # Update dp in reverse order to avoid using updated states in the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    new_mask = m | mask
                    dp[new_mask] = (dp[new_mask] + dp[m] * count[num]) % MOD

        result = sum(dp[1:]) % MOD
        return result