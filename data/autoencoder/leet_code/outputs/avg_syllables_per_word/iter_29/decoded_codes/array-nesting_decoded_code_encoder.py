class Solution:
    def arrayNesting(self, nums):
        visited_list = [False] * len(nums)
        maximum_length = 0

        for index in range(len(nums)):
            if not visited_list[index]:
                current_length = 0
                k = index
                while not visited_list[k]:
                    visited_list[k] = True
                    k = nums[k]
                    current_length += 1
                if maximum_length < current_length:
                    maximum_length = current_length
        return maximum_length