from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums):
        MOD = 10 ** 9 + 7

        # Map of primes considered and their positions (1-based)
        prime_to_pos = {
            2: 1,
            3: 2,
            5: 3,
            7: 4,
            11: 5,
            13: 6,
            17: 7,
            19: 8,
            23: 9,
            29: 10
        }

        # Precomputed prime factorization without repeated primes (only primes from above) for numbers <=30, since problem likely deals with nums in this range
        # Number -> list of prime factors (distinct, no repeats allowed because we want good subset)
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

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle count of 1's separately
        if 1 in count:
            dp[0] = pow(2, count[1], MOD)

        for num in count:
            if num == 1:
                continue

            # Only consider numbers that do not have repeated prime factors and are included in prime_factors
            if num not in prime_factors:
                continue

            factors = prime_factors[num]

            # Check for repeated prime factor in num: if num includes the same prime factor multiple times, skip
            # (already done by limiting prime_factors to numbers without repeated prime factors)

            mask = 0
            for prime in factors:
                mask |= 1 << (prime_to_pos[prime] - 1)

            # Update dp in reverse order to avoid using updated states in the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % MOD

        result = sum(dp[1:]) % MOD
        return result