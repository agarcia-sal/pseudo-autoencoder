from collections import Counter

class Solution:
    MOD = 10 ** 9 + 7
    prime_factors = {
        2: [1],
        3: [0, 1],
        5: [2, 1],
        6: [1],
        7: [3],
        10: [2, 1],
        11: [4],
        13: [0, 4],
        14: [3],
        15: [2, 0, 1],
        17: [5],
        19: [6],
        21: [3, 0, 1],
        22: [6, 4],
        23: [7],
        26: [6, 0, 4],
        29: [8],
        30: [2, 1, 0],
    }

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        max_mask = 1 << 10
        dp = [0] * max_mask
        dp[0] = 1

        for num, freq in count.items():
            if num == 1:
                dp[0] = (dp[0] * pow(2, freq, self.MOD)) % self.MOD
                continue
            if num not in self.prime_factors:
                continue

            factors = self.prime_factors[num]
            mask = 0
            for prime in factors:
                mask |= 1 << (prime - 1)

            for m in range(max_mask - 1, -1, -1):
                if m & mask == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % self.MOD

        return sum(dp[1:]) % self.MOD