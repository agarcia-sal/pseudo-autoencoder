from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        frequency_map = Counter(nums)
        maximum_frequency = max(frequency_map.values()) if frequency_map else 0
        length_of_nums = len(nums)
        division_result = length_of_nums // k
        return division_result >= maximum_frequency