from collections import Counter
from typing import List

MOD = 10**9 + 7

# Prime numbers up to 30 (since problem typically involves numbers up to 30)
# We use their indices from 0 to 9 to create bitmasks (10 primes)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def get_prime_factor_mask(num: int) -> int:
    """
    Returns a bitmask representing the unique prime factors of num.
    If num has a squared prime factor, return 0 (invalid),
    since numbers with squared factors do not form a good subset.
    """
    mask = 0
    for i, p in enumerate(PRIMES):
        count = 0
        while num % p == 0:
            num //= p
            count += 1
            if count > 1:
                return 0  # squared prime factor found, invalid
        if count == 1:
            mask |= (1 << i)
    if num > 1:
        # num is prime > 29, but problem constraints or prime_factors should cover up to 30, so ignore
        # (If num > 1 here, means prime factor > 29 not in PRIMES -> discard)
        return 0
    return mask


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        # dp[mask]: number of subsets with prime factors represented by mask
        dp = [0] * (1 << 10)
        dp[0] = 1  # empty subset

        freq_one = count.get(1, 0)
        # Precompute powers of two for freq_one
        pow2_one = pow(2, freq_one, MOD)

        # Precompute masks for each unique num except 1 for efficiency
        # Also skip nums that are invalid (mask=0)
        for num, freq in count.items():
            if num == 1:
                continue
            mask = get_prime_factor_mask(num)
            if mask == 0:
                continue

            # Iterate backward to avoid using updated dp in this iteration
            for m in range((1 << 10) - 1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq) % MOD

        # Multiply dp[0] by 2^freq_one (all subsets from ones)
        dp[0] = dp[0] * pow2_one % MOD

        # Sum all subsets except empty subset (mask=0)
        return (sum(dp) - dp[0]) % MOD