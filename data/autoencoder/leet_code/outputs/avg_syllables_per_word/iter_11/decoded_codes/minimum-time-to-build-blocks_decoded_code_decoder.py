from heapq import heapify, heappop, heappush

class Solution:
    def minBuildTime(self, blocks, split):
        heapify(blocks)
        while len(blocks) > 1:
            first = heappop(blocks)
            second = heappop(blocks)
            combined_time = split + second
            heappush(blocks, combined_time)
        return blocks[0]