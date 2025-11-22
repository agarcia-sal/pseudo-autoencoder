class Solution:
    def findMaxLength(self, list_of_numbers):
        prefix_sum_index = {0: -1}
        max_length = 0
        count = 0

        for index, number in enumerate(list_of_numbers):
            if number == 1:
                count += 1
            else:
                count -= 1

            if count in prefix_sum_index:
                max_length = max(max_length, index - prefix_sum_index[count])
            else:
                prefix_sum_index[count] = index

        return max_length