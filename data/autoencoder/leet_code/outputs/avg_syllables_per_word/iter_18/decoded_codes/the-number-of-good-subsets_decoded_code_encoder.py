from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        # Prime factorization mask for valid numbers from 2 to 30 excluding multiples of any squared prime
        prime_factors_map = {
            2: [0],
            3: [1],
            5: [2],
            6: [0,1],    # 2*3
            7: [3],
            10: [0,2],   # 2*5
            11: [4],
            13: [5],
            14: [0,3],   # 2*7
            15: [1,2],   # 3*5
            17: [6],
            19: [7],
            21: [1,3],   # 3*7
            22: [0,4],   # 2*11
            23: [8],
            26: [0,5],   # 2*13
            29: [9],
            30: [0,1,2], # 2*3*5
            9: [],       # 3^2 excluded from prime_factors_map
            4: [],       # 2^2 excluded
            8: [],       # 2^3 excluded
            12: [],      # 2^2*3 excluded
            18: [],      # 2*3^2 excluded
            20: [],      # 2^2*5 excluded
            24: [],      # 2^3*3 excluded
            25: [],      # 5^2 excluded
            27: [],      # 3^3 excluded
            28: []       # 2^2*7 excluded
        }

        # To filter out numbers containing squared prime factors, we remove from map those with empty factors
        prime_factors_map = {k:v for k,v in prime_factors_map.items() if v}

        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Handle the count of 1 separately
        ones_count = count.get(1, 0)
        if ones_count:
            dp[0] = pow(2, ones_count, MOD)

        for num, freq in count.items():
            if num == 1:
                continue
            if num not in prime_factors_map:
                # skip numbers with squared prime factors or numbers outside 2-30 range or no factor mapping
                continue

            factors = prime_factors_map[num]
            mask = 0
            for prime_index in factors:
                mask |= 1 << prime_index

            # Traverse dp backwards to avoid reuse in the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % MOD

        # Sum all dp states except the empty subset at dp[0]
        return sum(dp[1:]) % MOD