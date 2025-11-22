from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values()) if freq else 0
        length_divided_by_k = len(nums) // k
        return length_divided_by_k >= max_freq