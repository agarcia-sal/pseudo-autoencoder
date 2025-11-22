import heapq

def minBuildTime(blocks, split):
    heapq.heapify(blocks)
    while len(blocks) > 1:
        a = heapq.heappop(blocks)
        b = heapq.heappop(blocks)
        heapq.heappush(blocks, split + max(a, b))
    return blocks[0]