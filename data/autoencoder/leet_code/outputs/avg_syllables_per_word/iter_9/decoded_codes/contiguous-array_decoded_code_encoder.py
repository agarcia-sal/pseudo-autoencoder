class Solution:
    def findMaxLength(self, nums):
        prefix_sum_index = {0: -1}
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in prefix_sum_index:
                max_length = max(max_length, i - prefix_sum_index[count])
            else:
                prefix_sum_index[count] = i

        return max_length