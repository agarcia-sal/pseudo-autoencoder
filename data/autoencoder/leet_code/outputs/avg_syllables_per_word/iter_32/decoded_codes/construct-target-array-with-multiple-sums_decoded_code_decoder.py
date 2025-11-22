import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        total_sum = sum(target)

        while -max_heap[0] > 1:
            largest = -heapq.heappop(max_heap)
            rest_sum = total_sum - largest

            # If largest is less than or equal to rest_sum or rest_sum is zero, 
            # it's impossible to form the array
            if largest <= rest_sum or rest_sum == 0:
                return False

            new_value = largest % rest_sum

            # If new_value is zero and rest_sum is not one,
            # we cannot form the target array
            if new_value == 0 and rest_sum != 1:
                return False

            total_sum = rest_sum + new_value
            heapq.heappush(max_heap, -new_value)

        return True