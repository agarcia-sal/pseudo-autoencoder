from collections import Counter

class Solution:
    MOD = 10**9 + 7
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
        15: [3, 5]
    }
    # Since problem uses primes 1-based indexing up to 10 primes (2,3,5,7,11,13,17,19,23,29),
    # but problem data only contains primes up to 13/15, following pseudocode's 10 bits:
    # For mapping prime to bit position (prime-1), ensure primes are from 1..10.
    # To fully replicate pseudocode, we restrict to primes in prime_factors keys.

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num, c in count.items():
            if num == 1:
                dp[0] = dp[0] * pow(2, c, self.MOD) % self.MOD
                continue
            if num not in self.prime_factors:
                continue
            factors = self.prime_factors[num]

            mask = 0
            for prime in factors:
                mask |= 1 << (prime - 1)

            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % self.MOD

        return sum(dp[1:]) % self.MOD