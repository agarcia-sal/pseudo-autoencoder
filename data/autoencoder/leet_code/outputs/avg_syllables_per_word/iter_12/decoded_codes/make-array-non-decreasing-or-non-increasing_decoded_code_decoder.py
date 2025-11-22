import heapq

class Solution:
    def convertArray(self, nums):
        def min_operations_to_non_decreasing(nums):
            max_heap = []
            operations = 0
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    largest = -heapq.heappop(max_heap)
                    operations += largest - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)
            return operations

        def min_operations_to_non_increasing(nums):
            min_heap = []
            operations = 0
            for num in nums:
                if min_heap and min_heap[0] < num:
                    smallest = heapq.heappop(min_heap)
                    operations += num - smallest
                    heapq.heappush(min_heap, num)
                heapq.heappush(min_heap, num)
            return operations

        result_to_non_decreasing = min_operations_to_non_decreasing(nums)
        result_to_non_increasing = min_operations_to_non_increasing(nums)
        return min(result_to_non_decreasing, result_to_non_increasing)