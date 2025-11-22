class Solution:
    def findMaxLength(self, nums):
        prefix_sum_index = {0: -1}
        max_length = 0
        count = 0

        for index, number in enumerate(nums):
            if number == 1:
                count += 1
            else:
                count -= 1

            if count in prefix_sum_index:
                possible_length = index - prefix_sum_index[count]
                if possible_length > max_length:
                    max_length = possible_length
            else:
                prefix_sum_index[count] = index

        return max_length