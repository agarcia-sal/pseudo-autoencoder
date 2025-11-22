import heapq

class Solution:
    def findKthLargest(self, list_of_numbers, k):
        minimum_heap = []
        for number in list_of_numbers:
            heapq.heappush(minimum_heap, number)
            if len(minimum_heap) > k:
                heapq.heappop(minimum_heap)
        return minimum_heap[0]