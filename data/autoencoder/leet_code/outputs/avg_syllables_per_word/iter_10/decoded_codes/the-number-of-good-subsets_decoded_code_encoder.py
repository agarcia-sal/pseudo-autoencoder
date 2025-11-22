class Solution:
    def numberOfGoodSubsets(self, nums):
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
            15: [3, 5],
            17: [17],
            19: [19],
            21: [3, 7],
            22: [2, 11],
            23: [23],
            26: [2, 13],
            29: [29],
            30: [2, 3, 5]
        }

        # Only certain numbers can form good subsets; numbers containing squared primes are discarded:
        # The problem expects this mapping based on constraints from "Leetcode 1994."
        # We only handle numbers <= 30 that don't have squared prime factors.
        # Others are ignored.

        from collections import Counter
        count = Counter(nums)

        # Primes considered: 2,3,5,7,11,13,17,19,23,29 (first 10 primes relevant)
        # So we can map these primes to bits 0 to 9:
        prime_to_bit = {2:0,3:1,5:2,7:3,11:4,13:5,17:6,19:7,23:8,29:9}
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in count:
            if num == 1:
                dp[0] = dp[0] * pow(2, count[1], MOD) % MOD
                continue
            if num not in prime_factors:
                continue
            mask = 0
            for p in prime_factors[num]:
                bit = prime_to_bit[p]
                if mask & (1 << bit):
                    # duplicate prime factor (should not happen in prime_factors dict)
                    mask = -1
                    break
                mask |= 1 << bit
            if mask == -1:
                continue
            c = count[num]
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MOD

        return sum(dp[1:]) % MOD