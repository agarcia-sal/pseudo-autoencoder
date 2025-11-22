from typing import List

class Solution:
    def findNumberOfLIS(self, list_of_numbers: List[int]) -> int:
        if not list_of_numbers:
            return 0

        total_length = len(list_of_numbers)
        lengths = [1] * total_length
        counts = [1] * total_length

        for i in range(total_length):
            for j in range(i):
                if list_of_numbers[i] > list_of_numbers[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        longest_length = max(lengths)
        total_count = 0
        for k in range(total_length):
            if lengths[k] == longest_length:
                total_count += counts[k]

        return total_count