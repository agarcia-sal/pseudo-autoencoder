from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, list_of_numbers, k):
        frequency_count = Counter(list_of_numbers)
        maximum_frequency = max(frequency_count.values())
        return len(list_of_numbers) // k >= maximum_frequency