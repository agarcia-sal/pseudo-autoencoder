from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        freq = Counter(nums)
        max_freq = max(freq.values())
        if len(nums) // k >= max_freq:
            return True
        else:
            return False