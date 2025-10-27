from collections import Counter

MOD = 10 ** 9 + 7

# Precomputed prime factor bitmasks for numbers 2 through 30 without repeated prime factors
# Only numbers whose prime factorization doesn't contain squared primes are included
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

# Map each prime to a unique bit position (10 primes total)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
prime_to_bit = {p: i for i, p in enumerate(primes)}


class Solution:
    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in count:
            if num == 1:
                # Subsets with 1 can be doubled for each occurrence of 1
                dp[0] = (dp[0] * pow(2, count[1], MOD)) % MOD
                continue

            if num not in prime_factors:
                # Skip numbers that have squared prime factors or are not in prime_factors
                continue

            # Create mask for num's prime factors
            mask = 0
            factors = prime_factors[num]
            # If any prime factor appears more than once (implies square), skip (already avoided)
            # Calculate mask bits
            for prime in factors:
                bit = prime_to_bit[prime]
                mask |= (1 << bit)

            # Update dp from high to low to avoid reuse within the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % MOD

        # sum all subsets except empty subset (dp[0] counts empty subset)
        result = sum(dp[1:]) % MOD
        return result