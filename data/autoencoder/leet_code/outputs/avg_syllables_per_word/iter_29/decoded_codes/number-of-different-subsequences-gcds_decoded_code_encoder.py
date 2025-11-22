from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums):
        maximum_number = max(nums)
        number_set = set(nums)
        count_of_gcds = 0
        for g in range(1, maximum_number + 1):
            gcd_value = 0
            for m in range(g, maximum_number + 1, g):
                if m in number_set:
                    gcd_value = gcd(gcd_value, m)
                    if gcd_value == g:
                        count_of_gcds += 1
                        break
        return count_of_gcds