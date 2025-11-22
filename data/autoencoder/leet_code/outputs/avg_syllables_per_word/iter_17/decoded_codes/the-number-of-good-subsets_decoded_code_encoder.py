from collections import Counter
from math import comb

class Solution:
    MOD = 10**9 + 7
    # List of primes up to 30 for factorization based on problem constraints (nums typically <= 30)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Precomputed mapping from num to its bitmask of prime factors, or 0 if invalid or repeated prime factor
        def get_prime_factors_mask(num):
            mask = 0
            for i, p in enumerate(self.primes):
                cnt = 0
                while num % p == 0:
                    num //= p
                    cnt += 1
                    if cnt > 1:
                        return 0  # prime factor repeated => invalid
                if cnt == 1:
                    mask |= (1 << i)
            return mask if num == 1 else 0  # if num not fully factorized it has primes > 29, invalid

        # Process number 1 separately (special case)
        if 1 in count:
            dp[0] = pow(2, count[1], self.MOD)

        for num in count:
            if num == 1:
                continue
            mask = get_prime_factors_mask(num)
            if mask == 0:
                continue
            freq = count[num]
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % self.MOD

        return sum(dp[1:]) % self.MOD