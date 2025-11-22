from collections import Counter

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

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        prime_to_bit = {}
        primes = [2,3,5,7,11,13,17,19,23,29]
        for i, p in enumerate(primes):
            prime_to_bit[p] = i

        for num, c in count.items():
            if num == 1:
                dp[0] = dp[0] * pow(2, c, MOD) % MOD
                continue

            if num not in prime_factors:
                continue

            # Check if num has any repeated prime factor (square factor)
            factors = prime_factors[num]
            # If any prime factor repeats, skip num
            # Since num given is from predefined prime_factors with no repeats, no need for this check

            mask = 0
            for prime in factors:
                mask |= 1 << prime_to_bit[prime]

            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MOD

        return (sum(dp[1:]) % MOD)