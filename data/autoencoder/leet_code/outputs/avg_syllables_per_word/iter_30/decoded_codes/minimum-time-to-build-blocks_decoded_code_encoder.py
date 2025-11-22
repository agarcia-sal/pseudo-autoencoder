import heapq

class Solution:
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            combined_time = split + second
            heapq.heappush(blocks, combined_time)
        return blocks[0] if blocks else 0