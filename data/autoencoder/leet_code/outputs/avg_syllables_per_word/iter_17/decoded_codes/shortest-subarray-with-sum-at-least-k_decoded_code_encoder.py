from collections import deque
from math import inf

class Solution:
    def shortestSubarray(self, list_of_numbers, threshold_k):
        prefix_sum_list = [0]
        for number in list_of_numbers:
            prefix_sum_list.append(prefix_sum_list[-1] + number)

        dq = deque()
        min_length_subarray = inf

        for i, current_sum_value in enumerate(prefix_sum_list):
            while dq and current_sum_value - prefix_sum_list[dq[0]] >= threshold_k:
                min_length_subarray = min(min_length_subarray, i - dq.popleft())

            while dq and current_sum_value <= prefix_sum_list[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if min_length_subarray == inf else min_length_subarray