from collections import Counter

MODULO = 10**9 + 7
# prime_factors maps each number (2 <= num <= 30) to a list of its prime factors (without repeats and no repeated prime factors allowed)
prime_factors = {
    2: [2],
    3: [3],
    4: [],   # has repeated factor 2*2, excluded
    5: [5],
    6: [2, 3],
    7: [7],
    8: [],   # 2*2*2 repeated prime factor 2 excluded
    9: [],   # 3*3 repeated prime factor 3 excluded
    10: [2, 5],
    11: [11],
    12: [],  # 2*2*3 repeated 2 excluded
    13: [13],
    14: [2, 7],
    15: [3, 5],
    16: [],  # 2*2*2*2 repeated 2 excluded
    17: [17],
    18: [],  # 2*3*3 repeated 3 excluded
    19: [19],
    20: [],  # 2*2*5 repeated 2 excluded
    21: [3, 7],
    22: [2, 11],
    23: [23],
    24: [],  # 2*2*2*3 repeated 2 excluded
    25: [],  # 5*5 repeated 5 excluded
    26: [2, 13],
    27: [],  # 3*3*3 repeated 3 excluded
    28: [],  # 2*2*7 repeated 2 excluded
    29: [29],
    30: [2, 3, 5],
}

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        # Map prime factors 2,3,5,7,11,13,17,19,23,29 to bits 0 to 9
        prime_to_bit = {2:0,3:1,5:2,7:3,11:4,13:5,17:6,19:7,23:8,29:9}

        for num in count:
            if num == 1:
                # 1 can be chosen any number of times without changing prime factors
                dp[0] = dp[0] * pow(2, count[1], MODULO) % MODULO
                continue
            if num not in prime_factors or not prime_factors[num]:
                continue

            factors = prime_factors[num]
            mask = 0
            # Build bitmask for prime factors of num
            for prime in factors:
                mask |= 1 << prime_to_bit[prime]

            c = count[num]
            # Iterate dp backwards to avoid reuse in the same iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * c) % MODULO

        # exclude empty subset
        return sum(dp[1:]) % MODULO