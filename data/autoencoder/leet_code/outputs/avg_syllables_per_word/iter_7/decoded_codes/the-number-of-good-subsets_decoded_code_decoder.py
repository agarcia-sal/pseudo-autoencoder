from typing import List
from collections import Counter

MOD = 10**9 + 7

prime_factors = {
    2: [2],
    3: [3],
    4: [2],
    5: [5],
    6: [2, 3],
    7: [7],
    8: [2],
    9: [3],
    10: [2, 5],
    11: [11],
    12: [2, 3],
    13: [13],
    14: [2, 7],
    15: [3, 5],
    16: [2],
    17: [17],
    18: [2, 3],
    19: [19],
    20: [2, 5],
    # Note: Given the original pseudocode and problem constraints might focus mostly on 1 to 30 or so.
    # But the prime_factors dict is required as given; if more numbers beyond need to be supported,
    # additional prime factor info should be added.
}

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in count.keys():
            if num == 1:
                dp[0] = (dp[0] * pow(2, count[num], MOD)) % MOD
                continue
            if num not in prime_factors:
                continue
            factors = prime_factors[num]
            mask = 0
            for prime in factors:
                mask |= 1 << (prime - 1)
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % MOD

        result = sum(dp[1:]) % MOD
        return result