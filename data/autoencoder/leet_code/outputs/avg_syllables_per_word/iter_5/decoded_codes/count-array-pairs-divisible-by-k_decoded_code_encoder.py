from math import gcd
from collections import Counter

class Solution:
    def countPairs(self, nums, k):
        gcd_count = Counter(gcd(num, k) for num in nums)
        gcd_values = list(gcd_count)
        total_pairs = 0
        n = len(gcd_values)

        for i in range(n):
            for j in range(i, n):
                gcd1, gcd2 = gcd_values[i], gcd_values[j]
                if (gcd1 * gcd2) % k == 0:
                    if i == j:
                        total_pairs += gcd_count[gcd1] * (gcd_count[gcd1] - 1) // 2
                    else:
                        total_pairs += gcd_count[gcd1] * gcd_count[gcd2]

        return total_pairs