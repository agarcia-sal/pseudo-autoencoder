from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        max_num = max(nums)
        num_set = set(nums)
        count = 0

        for g in range(1, max_num + 1):
            current_gcd = 0
            for multiple in range(g, max_num + 1, g):
                if multiple in num_set:
                    current_gcd = gcd(current_gcd, multiple)
                    if current_gcd == g:
                        count += 1
                        break

        return count