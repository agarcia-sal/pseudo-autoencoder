class Solution:
    def maxChunksToSorted(self, arr):
        max_so_far = 0
        chunks = 0

        for i, val in enumerate(arr):
            max_so_far = max(max_so_far, val)
            if max_so_far == i:
                chunks += 1

        return chunks