from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        frequency_counter = Counter(nums)
        maximum_frequency = max(frequency_counter.values()) if frequency_counter else 0
        length_of_list = len(nums)
        quotient = length_of_list // k
        return quotient >= maximum_frequency