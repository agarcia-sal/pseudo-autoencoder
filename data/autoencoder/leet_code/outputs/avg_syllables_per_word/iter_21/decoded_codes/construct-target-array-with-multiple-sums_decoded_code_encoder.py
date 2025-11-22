import heapq

class Solution:
    def isPossible(self, target):
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)

        total_sum = sum(target)

        while -max_heap[0] > 1:
            largest = -heapq.heappop(max_heap)
            rest_sum = total_sum - largest

            if largest <= rest_sum or rest_sum == 0:
                return False

            new_value = largest % rest_sum

            if new_value == 0 and rest_sum != 1:
                return False

            total_sum = rest_sum + new_value
            heapq.heappush(max_heap, -new_value)

        return True