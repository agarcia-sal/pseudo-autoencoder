from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums):
        MOD = 10**9 + 7
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

        # The problem context implies that only nums in 1..30 can appear
        # and only subset of these with no repeated prime factor can be considered

        count = Counter(nums)

        # Primes used are first 10 primes: 2,3,5,7,11,13,17,19,23,29
        primes = [2,3,5,7,11,13,17,19,23,29]

        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle 1s separately at the end as they only double count without changing subset composition
        ones_count = count.get(1,0)

        for num, c in count.items():
            if num == 1 or num not in prime_factors:
                continue
            factors = prime_factors[num]
            mask = 0
            valid = True
            for p in factors:
                idx = primes.index(p)
                if (mask & (1 << idx)) != 0:
                    valid = False
                    break
                mask |= (1 << idx)
            if not valid:
                continue
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0 and dp[m] != 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MOD

        result = sum(dp[1:]) % MOD
        result = (result * pow(2, ones_count, MOD)) % MOD
        return result