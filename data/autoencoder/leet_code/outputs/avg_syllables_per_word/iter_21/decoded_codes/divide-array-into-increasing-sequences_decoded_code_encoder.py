from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        freq = Counter(nums)
        max_freq = max(freq.values(), default=0)
        division_result = len(nums) // k
        return division_result >= max_freq