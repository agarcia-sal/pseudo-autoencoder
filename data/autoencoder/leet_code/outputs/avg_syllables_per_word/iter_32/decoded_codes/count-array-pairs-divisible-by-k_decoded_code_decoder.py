import math
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Count frequencies of gcd(num, k) for each num in nums
        gcd_count = Counter()
        for num in nums:
            g = math.gcd(num, k)
            gcd_count[g] += 1

        gcd_values = list(gcd_count.keys())
        n = len(gcd_values)
        total_pairs = 0

        # Iterate over all pairs (including pairs with same gcd)
        for i in range(n):
            gcd1 = gcd_values[i]
            cnt1 = gcd_count[gcd1]
            for j in range(i, n):
                gcd2 = gcd_values[j]
                cnt2 = gcd_count[gcd2]

                # Check if product of gcd1 and gcd2 is divisible by k
                if (gcd1 * gcd2) % k == 0:
                    if i == j:
                        # combinations of two from cnt1
                        total_pairs += cnt1 * (cnt1 - 1) // 2
                    else:
                        total_pairs += cnt1 * cnt2

        return total_pairs