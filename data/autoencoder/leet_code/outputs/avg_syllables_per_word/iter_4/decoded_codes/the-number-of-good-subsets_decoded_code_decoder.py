from collections import Counter

class Solution:
    MOD = 10**9 + 7
    # Predefined prime factors for numbers up to 30 without square factors:
    # Only consider numbers whose prime factors do not repeat (i.e., square-free numbers).
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

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)  # 2^10 because we have 10 primes max (for primes up to 30)
        dp[0] = 1

        for num in count:
            if num == 1:
                # All subsets can always include 1 without affecting prime factorization
                dp[0] = (dp[0] * pow(2, count[1], self.MOD)) % self.MOD
                continue

            if num not in self.prime_factors:
                # Skip numbers that have squared prime factors or are not in prime_factors
                continue

            factors = self.prime_factors[num]
            mask = 0
            for prime in factors:
                mask |= 1 << (prime - 1)

            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % self.MOD

        return sum(dp[1:]) % self.MOD