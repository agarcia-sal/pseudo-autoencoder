class Solution:
    def maxChunksToSorted(self, arr):
        max_so_far = 0
        chunks = 0
        for i in range(len(arr)):
            if arr[i] > max_so_far:
                max_so_far = arr[i]
            if max_so_far == i:
                chunks += 1
        return chunks