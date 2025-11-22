from collections import Counter

prime_factors = {
    2: [2],
    3: [3],
    4: [2],
    5: [5],
    6: [2, 3],
    7: [7],
    8: [2],
    9: [3],
    10: [2, 5]
}

MOD = 10**9 + 7

def count_prime_subsets(nums):
    count = Counter(nums)
    dp = [0] * (1 << 10)
    dp[0] = 1

    for num in count:
        if num == 1:
            dp[0] = dp[0] * pow(2, count[1], MOD) % MOD
        elif num in prime_factors:
            mask = 0
            for p in prime_factors[num]:
                mask |= 1 << (p - 1)
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * count[num]) % MOD

    return sum(dp[1:]) % MOD