from collections import Counter

class Solution:
    MOD = 10**9 + 7
    prime_factors = {
        2: [1],
        3: [2],
        5: [3],
        6: [1, 2],  # 6 = 2 * 3
        7: [4],
        10: [1, 3], # 10 = 2 * 5
        11: [5],
        13: [6],
        14: [1, 4], # 14 = 2 * 7
        15: [2, 3], # 15 = 3 * 5
        17: [7],
        19: [8],
        21: [2, 4], # 21 = 3 * 7
        22: [1, 5], # 22 = 2 * 11
        23: [9],
        26: [1, 6], # 26 = 2 * 13
        29: [10],
        30: [1, 2, 3], # 30 = 2 * 3 * 5
    }

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle factor masks with non-square-free check
        for num in count:
            if num == 1:
                dp[0] = (dp[0] * pow(2, count[1], self.MOD)) % self.MOD
                continue
            if num not in self.prime_factors:
                continue

            factors = self.prime_factors[num]
            mask = 0
            for prime in factors:
                mask |= 1 << (prime - 1)

            # Update dp in decreasing order to avoid double counting
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % self.MOD

        return sum(dp[1:]) % self.MOD