from collections import Counter

class Solution:
    MOD = 10**9 + 7

    # prime_factors dictionary mapping each num to a list of its prime factors without duplicates, 
    # specifically for numbers with square-free prime factorization within range [2..30]
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

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Mapping prime numbers to bit positions 0 to 9 for all primes <= 29 used above
        prime_to_bit = {
            2: 0,
            3: 1,
            5: 2,
            7: 3,
            11: 4,
            13: 5,
            17: 6,
            19: 7,
            23: 8,
            29: 9,
        }

        # Handle the number 1's count initially
        if 1 in count:
            dp[0] = pow(2, count[1], self.MOD)

        for num in count:
            if num == 1:
                continue
            if num not in self.prime_factors:
                # skip numbers with non-square free factorization or primes outside specified range
                continue

            factors = self.prime_factors[num]
            mask = 0
            # Build prime factor bitmask for current number
            conflict = False
            for prime in factors:
                bit = prime_to_bit[prime]
                if (mask >> bit) & 1:
                    # duplicate prime factor indicates square (not square-free), skip
                    conflict = True
                    break
                mask |= (1 << bit)
            if conflict:
                continue

            c = count[num]
            # Update dp from high to low to avoid double counting
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] += dp[m] * c
                    dp[m | mask] %= self.MOD

        result = sum(dp[1:]) % self.MOD
        return result