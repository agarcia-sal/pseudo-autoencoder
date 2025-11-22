from collections import deque
from math import inf
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum_list = [0]
        for num in nums:
            prefix_sum_list.append(prefix_sum_list[-1] + num)

        dq = deque()
        minimum_length = inf

        for i, current_sum in enumerate(prefix_sum_list):
            while dq and current_sum - prefix_sum_list[dq[0]] >= k:
                minimum_length = min(minimum_length, i - dq.popleft())

            while dq and current_sum <= prefix_sum_list[dq[-1]]:
                dq.pop()

            dq.append(i)

        return minimum_length if minimum_length != inf else -1