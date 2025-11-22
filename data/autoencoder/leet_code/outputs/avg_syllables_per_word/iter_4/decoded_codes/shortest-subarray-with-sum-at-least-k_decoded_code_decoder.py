from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        dq = deque()
        min_length = float('inf')

        for i, current_sum in enumerate(prefix_sum):
            while dq and current_sum - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            while dq and current_sum <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if min_length == float('inf') else min_length