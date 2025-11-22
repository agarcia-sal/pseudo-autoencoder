import heapq

class Solution:
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            heapq.heappush(blocks, split + second)
        return blocks[0]