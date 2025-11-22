from collections import Counter
from typing import List

MOD = 10**9 + 7

# Predefined prime factor masks for numbers 2 to 30 without repeated prime factors:
# Each bit corresponds to a prime factor at position (prime-1)
prime_factors = {
    2: [2],
    3: [3],
    5: [5],
    6: [2,3],
    7: [7],
    10: [2,5],
    11: [11],
    13: [13],
    14: [2,7],
    15: [3,5],
    17: [17],
    19: [19],
    21: [3,7],
    22: [2,11],
    23: [23],
    26: [2,13],
    29: [29],
    30: [2,3,5]
}

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        dp = [0] * (1 << 10)  # There are 10 primes considered, so 2^10 states
        dp[0] = 1

        for num, c in count.items():
            if num == 1:
                # The subset including only 1's multiply dp[0] by 2^count[1]
                # Each 1 can be included or excluded independently
                dp[0] = (dp[0] * pow(2, c, MOD)) % MOD
                continue

            if num not in prime_factors:
                # Number contains repeated prime factors or primes not in 2..30 list; skip
                continue

            # Build mask for number's prime factors
            mask = 0
            valid = True
            # Turn each prime into a bit: prime p map to bit (p-1)
            # But we need to verify no repeated bit set, which is guaranteed by above dict
            for prime in prime_factors[num]:
                bit = prime - 1
                if (mask & (1 << bit)) != 0:
                    valid = False  # repeated prime factor, skip this num
                    break
                mask |= (1 << bit)
            if not valid:
                continue

            # Update dp states in descending order to avoid double counting
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MOD

        return sum(dp[1:]) % MOD