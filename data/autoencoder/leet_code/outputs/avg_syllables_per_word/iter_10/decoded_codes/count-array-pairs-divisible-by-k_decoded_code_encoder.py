from collections import Counter
from math import gcd

class Solution:
    def countPairs(self, nums, k):
        gcd_count = Counter(gcd(num, k) for num in nums)
        total_pairs = 0
        gcd_values = list(gcd_count.keys())
        n = len(gcd_values)

        for i in range(n):
            for j in range(i, n):
                gcd1, gcd2 = gcd_values[i], gcd_values[j]
                if (gcd1 * gcd2) % k == 0:
                    if i == j:
                        count = gcd_count[gcd1]
                        total_pairs += count * (count - 1) // 2
                    else:
                        total_pairs += gcd_count[gcd1] * gcd_count[gcd2]

        return total_pairs