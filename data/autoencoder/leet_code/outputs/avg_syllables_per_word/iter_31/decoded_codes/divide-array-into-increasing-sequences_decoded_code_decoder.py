from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values(), default=0)
        return (len(nums) // k) >= max_freq