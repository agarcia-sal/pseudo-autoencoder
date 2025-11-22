from collections import Counter

MOD = 10**9 + 7

# Mapping each number to its prime factors without repetition, where primes are labeled 1 to 10 as per problem prime indexing
prime_factors = {
    2: [1],
    3: [2],
    5: [3],
    6: [1, 2],
    7: [4],
    10: [1, 3],
    11: [5],
    13: [6],
    14: [1, 4],
    15: [2, 3],
    17: [7],
    19: [8],
    21: [2, 4],
    22: [1, 5],
    23: [9],
    26: [1, 6],
    29: [10],
    30: [1, 2, 3]
}

class Solution:
    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in count:
            if num == 1:
                # Each 1 doubles the count of the empty subset choices
                dp[0] = dp[0] * pow(2, count[1], MOD) % MOD
                continue

            if num not in prime_factors:
                continue

            factors = prime_factors[num]
            mask = 0
            for prime in factors:
                # primes shifted by prime-1
                mask |= 1 << (prime - 1)

            # Iterate backwards to avoid using updated dp values in the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    new_mask = m | mask
                    dp[new_mask] = (dp[new_mask] + dp[m] * count[num]) % MOD

        result = sum(dp[1:]) % MOD
        return result