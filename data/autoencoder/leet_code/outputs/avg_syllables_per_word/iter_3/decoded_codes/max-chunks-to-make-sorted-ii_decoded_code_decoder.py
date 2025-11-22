class Solution:
    def maxChunksToSorted(self, arr):
        max_so_far = []
        current_max = arr[0]
        for num in arr:
            current_max = max(current_max, num)
            max_so_far.append(current_max)
        sorted_arr = sorted(arr)
        chunks = 0
        max_chunk = 0
        for i in range(len(arr)):
            max_chunk = max(max_chunk, arr[i])
            if max_chunk == sorted_arr[i]:
                chunks += 1
        return chunks