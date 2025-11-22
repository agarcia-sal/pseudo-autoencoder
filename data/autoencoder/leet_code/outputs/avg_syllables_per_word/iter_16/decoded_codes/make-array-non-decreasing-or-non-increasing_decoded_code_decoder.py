import heapq

class Solution:
    def convertArray(self, nums):
        def min_operations_to_non_decreasing(nums):
            max_heap = []
            operations = 0
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    prev = -heapq.heappop(max_heap)
                    operations += prev - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)
            return operations

        def min_operations_to_non_increasing(nums):
            min_heap = []
            operations = 0
            for num in nums:
                if min_heap and min_heap[0] < num:
                    prev = heapq.heappop(min_heap)
                    operations += num - prev
                    heapq.heappush(min_heap, num)
                heapq.heappush(min_heap, num)
            return operations

        return min(min_operations_to_non_decreasing(nums), min_operations_to_non_increasing(nums))