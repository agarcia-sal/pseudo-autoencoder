import heapq

class Solution:
    def convertArray(self, nums):
        def min_operations_to_non_decreasing(nums):
            max_heap = []
            operations = 0
            for number in nums:
                if max_heap and -max_heap[0] > number:
                    removed = -heapq.heappop(max_heap)
                    operations += removed - number
                    heapq.heappush(max_heap, -number)
                heapq.heappush(max_heap, -number)
            return operations

        def min_operations_to_non_increasing(nums):
            min_heap = []
            operations = 0
            for number in nums:
                if min_heap and min_heap[0] < number:
                    removed = heapq.heappop(min_heap)
                    operations += number - removed
                    heapq.heappush(min_heap, number)
                heapq.heappush(min_heap, number)
            return operations

        return min(min_operations_to_non_decreasing(nums), min_operations_to_non_increasing(nums))