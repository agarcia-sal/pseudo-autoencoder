from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values()) if freq else 0
        length_of_nums = len(nums)
        return (length_of_nums // k) >= max_freq