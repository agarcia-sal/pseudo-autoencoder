from collections import Counter

class Solution:
    MOD = 10**9 + 7

    # prime_factors maps numbers to the list of primes (1-based indices) representing their prime factors.
    # The problem typically involves numbers up to 30, with prime factors chosen from the first 10 primes.
    # We'll encode primes as bits 0 through 9 corresponding to primes 2,3,5,7,11,13,17,19,23,29
    # Only numbers with square-free prime factorization considered.
    # This mapping is based on known constraints problem variants: 
    # For example the LeetCode problem "The Number of Good Subsets"
    prime_factors = {
        2:  [1],        # prime 2 is index 1 for mask bit; note pseudocode uses prime-1 as bit index
        3:  [2],
        5:  [4],
        6:  [1,2],      # 2 * 3
        7:  [6],
        10: [1,4],      # 2 * 5
        11: [7],
        13: [8],
        14: [1,6],      # 2 * 7
        15: [2,4],      # 3 * 5
        17: [9],
        19: [10],
        21: [2,6],      # 3 * 7
        22: [1,7],      # 2 * 11
        23: [11],
        26: [1,8],      # 2 *13
        29: [12],
        30: [1,2,4],    # 2 * 3 * 5
    }

    # However, above indices go beyond 10 bits, we must map primes 2,3,5,7,11,13,17,19,23,29 to bits 0-9:
    # Let's define the prime list in order for bit assignment:
    _primes = [2,3,5,7,11,13,17,19,23,29]

    # We'll create a dictionary that maps number to primes by bit indices 0 to 9
    # only include numbers from 2 to 30 that are square-free and whose prime factors all in _primes
    # Skip numbers with repeated prime factors (square factors)
    # Let's create this mapping accordingly:

    # Create prime_factors map correctly from scratch:
    # Helper to factorize numbers and check if square-free and all prime factors in _primes

    @classmethod
    def _generate_prime_factors(cls):
        prime_set = set(cls._primes)
        pf = {}
        for num in range(2,31):
            n = num
            factors = []
            square_free = True
            for idx, p in enumerate(cls._primes):
                count_p = 0
                while n % p == 0:
                    n //= p
                    count_p += 1
                    if count_p > 1:
                        square_free = False
                        break
                if count_p == 1:
                    factors.append(idx)
                if not square_free:
                    break
            if n == 1 and square_free and factors:
                pf[num] = factors
        return pf

    prime_factors = _generate_prime_factors.__func__()

    def numberOfGoodSubsets(self, nums):
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        freq_one = count.get(1,0)
        if freq_one > 0:
            # Multiply dp[0] by 2^freq_one mod MOD to account for subsets of 1's
            dp[0] = pow(2, freq_one, self.MOD)

        for num in count:
            if num == 1:
                # Already handled
                continue
            if num not in self.prime_factors:
                # Number not valid (e.g. has squared prime factors or prime factors outside the set)
                continue
            mask = 0
            for prime_bit in self.prime_factors[num]:
                bit = 1 << prime_bit
                mask |= bit

            freq_num = count[num]
            # Traverse dp backwards to avoid recomputing states we just updated in this iteration
            for m in range(len(dp)-1, -1, -1):
                if (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + dp[m] * freq_num) % self.MOD

        # sum all dp except dp[0]
        return sum(dp[1:]) % self.MOD