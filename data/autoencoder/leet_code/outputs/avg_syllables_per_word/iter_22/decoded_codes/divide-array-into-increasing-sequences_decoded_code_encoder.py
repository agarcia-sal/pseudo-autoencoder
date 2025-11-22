from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        frequency_dictionary = Counter(nums)
        maximum_frequency = max(frequency_dictionary.values(), default=0)
        length_of_nums = len(nums)
        if length_of_nums // k >= maximum_frequency:
            return True
        else:
            return False