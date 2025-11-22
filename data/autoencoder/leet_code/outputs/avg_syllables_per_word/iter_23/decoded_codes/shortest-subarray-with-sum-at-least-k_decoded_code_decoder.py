from collections import deque
from math import inf
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        dq = deque()
        min_length = inf

        for i, current_sum in enumerate(prefix_sum):
            while dq and current_sum - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            while dq and current_sum <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)

        return min_length if min_length != inf else -1