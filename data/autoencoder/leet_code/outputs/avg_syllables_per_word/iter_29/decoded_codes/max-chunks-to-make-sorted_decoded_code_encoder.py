class Solution:
    def maxChunksToSorted(self, arr):
        maximum_value_observed_so_far = 0
        count_of_chunks = 0
        for index in range(len(arr)):
            maximum_value_observed_so_far = max(maximum_value_observed_so_far, arr[index])
            if maximum_value_observed_so_far == index:
                count_of_chunks += 1
        return count_of_chunks