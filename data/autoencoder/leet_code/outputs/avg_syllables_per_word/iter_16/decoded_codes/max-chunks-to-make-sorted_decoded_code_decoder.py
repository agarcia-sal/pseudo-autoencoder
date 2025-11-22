class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max_so_far = 0
        chunks = 0
        for index in range(len(arr)):
            max_so_far = max(max_so_far, arr[index])
            if max_so_far == index:
                chunks += 1
        return chunks