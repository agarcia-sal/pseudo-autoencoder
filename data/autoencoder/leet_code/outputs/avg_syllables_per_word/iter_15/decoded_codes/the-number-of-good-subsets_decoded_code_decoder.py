from collections import Counter

MODULO = 10**9 + 7
MAX_MASK = 1 << 10  # 2**10

# Predefined prime factorization mapping as per problem constraints.
# Since pseudocode refers to a predefined mapping but does not provide it,
# we define it here for numbers 2 <= num <= 30 (commonly used in such problems).
# The prime factors are distinct primes from the set:
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Only numbers without repeated prime factors (square-free) are included.

prime_factor_map = {
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

class Solution:
    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * MAX_MASK
        dp[0] = 1

        for num in count:
            if num == 1:
                dp[0] = (dp[0] * pow(2, count[1], MODULO)) % MODULO
                continue
            if num not in prime_factor_map:
                continue

            factors = prime_factor_map[num]
            mask = 0
            for prime in factors:
                # prime - 1 because primes used as bit indices are 1-based in pseudocode
                mask |= 1 << (prime - 1)

            # Traverse from high to low to not overwrite dp states needed in this iteration
            for m in range(MAX_MASK - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % MODULO

        result = sum(dp[1:]) % MODULO
        return result