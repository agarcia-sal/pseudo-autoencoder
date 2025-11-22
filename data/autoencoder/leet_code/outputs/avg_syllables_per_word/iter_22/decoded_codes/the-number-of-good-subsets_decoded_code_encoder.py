from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums):
        MOD = 10**9 + 7

        # Predefined prime factors for numbers up to 30 (since problem context often limits to 30)
        # and excluding numbers with squared prime factors as they can't be part of good subsets.
        prime_factors = {
            2: [1],       # Using 0-based indexing: 2^0 = 1<<0, but to avoid confusion use primes as indexes 0-9
            3: [2],
            5: [4],
            6: [1, 2],
            7: [6],
            10: [1, 4],
            11: [7],
            13: [8],
            14: [1, 6],
            15: [2, 4],
            17: [9],
            19: [10],
            21: [2, 6],
            22: [1, 7],
            23: [11],
            26: [1, 8],
            29: [12],
            30: [1, 2, 4, 6]
        }

        # Identifying primes from 2 to 30 with their indexes (0 to 9)
        # Since the problem used two**10, so presumably 10 primes, lets define them:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_to_index = {p: i for i, p in enumerate(primes)}

        # Adjust prime_factors to use bit positions instead of arbitrary numbers
        # The pseudocode implied "mask plus 2^(prime - 1)" which suggests 1-based indexing primes.
        # We will map each prime factor to its bit index.
        # We must filter nums with square factors i.e. not in prime_factors.

        # For clarity: The original pseudocode likely has a prebuilt prime_factors dictionary similar to LeetCode 1994

        # Construct prime_factors for numbers 2-30 excluding those with square factors:
        def get_prime_mask(num):
            # Return the bit mask representing the num's prime factors if no repeated prime factors (square factor)
            mask = 0
            for i, p in enumerate(primes):
                count = 0
                temp = num
                while temp % p == 0:
                    temp //= p
                    count += 1
                if count > 1:
                    return 0  # square factor, exclude
                if count == 1:
                    mask |= (1 << i)
            if temp != 1:
                # num contains prime factors not in primes list
                return 0
            return mask

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num, c in count.items():
            if num == 1:
                # Each 1 can either be included or not independently, doubles subsets count
                dp[0] = dp[0] * pow(2, c, MOD) % MOD
                continue

            mask = get_prime_mask(num)
            if mask == 0:
                # num has square factors or invalid prime factors; skip
                continue

            # Traverse dp backwards to avoid double counting
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MOD

        # sum all subsets except empty set (dp[0])
        return (sum(dp) - dp[0]) % MOD