import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        total_sum = sum(target)

        while True:
            largest = -heapq.heappop(max_heap)
            rest_sum = total_sum - largest

            if largest == 1 or rest_sum == 1:
                return True

            if largest <= rest_sum or rest_sum == 0:
                return False

            new_value = largest % rest_sum

            if new_value == 0 and rest_sum != 1:
                return False

            total_sum = rest_sum + new_value
            heapq.heappush(max_heap, -new_value)

            if max_heap[0] == -1:
                return True