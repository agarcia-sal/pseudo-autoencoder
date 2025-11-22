from collections import Counter
from math import gcd
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_count = Counter()
        for num in nums:
            gcd_value = gcd(num, k)
            gcd_count[gcd_value] += 1

        total_pairs = 0
        gcd_values = list(gcd_count.keys())
        n = len(gcd_values)

        for i in range(n):
            gcd1 = gcd_values[i]
            count1 = gcd_count[gcd1]
            for j in range(i, n):
                gcd2 = gcd_values[j]
                if (gcd1 * gcd2) % k == 0:
                    count2 = gcd_count[gcd2]
                    if i == j:
                        total_pairs += count1 * (count1 - 1) // 2
                    else:
                        total_pairs += count1 * count2

        return total_pairs