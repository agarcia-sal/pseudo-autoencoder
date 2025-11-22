from collections import deque
from math import inf

class Solution:
    def shortestSubarray(self, list_of_numbers, threshold_k):
        prefix_sum_array = [0]
        for number in list_of_numbers:
            prefix_sum_array.append(prefix_sum_array[-1] + number)

        dq = deque()
        minimum_length = inf

        for index, current_sum in enumerate(prefix_sum_array):
            while dq and current_sum - prefix_sum_array[dq[0]] >= threshold_k:
                candidate_length = index - dq.popleft()
                if candidate_length < minimum_length:
                    minimum_length = candidate_length

            while dq and current_sum <= prefix_sum_array[dq[-1]]:
                dq.pop()

            dq.append(index)

        return -1 if minimum_length == inf else minimum_length