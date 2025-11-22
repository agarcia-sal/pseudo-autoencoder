class Solution:
    def findNumberOfLIS(self, list_of_numbers):
        if not list_of_numbers:
            return 0
        n = len(list_of_numbers)
        lengths = self.initialize_list_with_value(1, n)
        counts = self.initialize_list_with_value(1, n)
        for i in range(n):
            for j in range(i):
                if list_of_numbers[i] > list_of_numbers[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        longest_length = max(lengths)
        total_count = 0
        for i in range(n):
            if lengths[i] == longest_length:
                total_count += counts[i]
        return total_count

    def initialize_list_with_value(self, value, count):
        return [value] * count