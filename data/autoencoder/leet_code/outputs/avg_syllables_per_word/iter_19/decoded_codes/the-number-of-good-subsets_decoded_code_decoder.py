from collections import Counter

MOD = 10**9 + 7

class Solution:
    def numberOfGoodSubsets(self, nums):
        # Mapping of prime to bit position (0-based)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_to_bit = {p: i for i, p in enumerate(primes)}

        # Precompute prime factors with no repeated prime factor and set mask
        prime_factors = {}
        for num in range(2, 31):
            # Factorization check for square-free and factor mask
            x = num
            mask = 0
            is_valid = True
            for p in primes:
                count_p = 0
                while x % p == 0:
                    x //= p
                    count_p += 1
                if count_p > 1:
                    is_valid = False
                    break
                if count_p == 1:
                    mask |= 1 << prime_to_bit[p]
            if is_valid and x == 1:
                prime_factors[num] = mask

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle 1s separately
        if 1 in count:
            dp[0] = pow(2, count[1], MOD)

        for num, freq in count.items():
            if num == 1:
                continue
            if num not in prime_factors:
                continue
            mask = prime_factors[num]
            # Iterate in reverse to avoid overwrite using results from same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % MOD

        return sum(dp[1:]) % MOD