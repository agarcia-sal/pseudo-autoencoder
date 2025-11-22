import heapq

def push_element_in_heap(heap, element):
    heapq.heappush(heap, element)

def pop_element_from_heap(heap):
    heapq.heappop(heap)

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        for num in nums:
            push_element_in_heap(min_heap, num)
            if len(min_heap) > k:
                pop_element_from_heap(min_heap)
        return min_heap[0]