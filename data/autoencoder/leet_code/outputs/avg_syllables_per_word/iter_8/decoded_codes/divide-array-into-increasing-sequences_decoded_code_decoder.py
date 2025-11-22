from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        freq = Counter(nums)
        max_freq = max(freq.values()) if freq else 0
        return len(nums) // k >= max_freq