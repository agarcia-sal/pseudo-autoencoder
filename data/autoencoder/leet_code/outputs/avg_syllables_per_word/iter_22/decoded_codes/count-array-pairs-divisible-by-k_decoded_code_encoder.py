from collections import Counter
from math import gcd

class Solution:
    def countPairs(self, nums, k):
        gcd_count = Counter()
        for num in nums:
            gcd_val = gcd(num, k)
            gcd_count[gcd_val] += 1

        total_pairs = 0
        gcd_values = list(gcd_count.keys())
        n = len(gcd_values)
        for i in range(n):
            gcd1 = gcd_values[i]
            for j in range(i, n):
                gcd2 = gcd_values[j]
                if (gcd1 * gcd2) % k == 0:
                    if i == j:
                        c = gcd_count[gcd1]
                        total_pairs += c * (c - 1) // 2
                    else:
                        total_pairs += gcd_count[gcd1] * gcd_count[gcd2]

        return total_pairs