class Solution:
    def maxChunksToSorted(self, arr):
        maximum_value_so_far = 0
        chunk_count = 0

        for index in range(len(arr)):
            maximum_value_so_far = max(maximum_value_so_far, arr[index])
            if maximum_value_so_far == index:
                chunk_count += 1

        return chunk_count