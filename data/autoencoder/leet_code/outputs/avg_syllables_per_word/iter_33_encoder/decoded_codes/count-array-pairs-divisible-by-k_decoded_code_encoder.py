from math import gcd
from collections import defaultdict

class Solution:
    def countPairs(self, nums, k):
        gcd_count = defaultdict(int)
        for num in nums:
            current_gcd = gcd(num, k)
            gcd_count[current_gcd] += 1

        total_pairs = 0
        gcd_values = list(gcd_count.keys())
        n = len(gcd_values)

        for i in range(n):
            for j in range(i, n):
                gcd1 = gcd_values[i]
                gcd2 = gcd_values[j]
                product = gcd1 * gcd2
                if product % k == 0:
                    if i == j:
                        count = gcd_count[gcd1]
                        # count choose 2
                        pairs_for_this = count * (count - 1) // 2
                        total_pairs += pairs_for_this
                    else:
                        count1 = gcd_count[gcd1]
                        count2 = gcd_count[gcd2]
                        total_pairs += count1 * count2

        return total_pairs