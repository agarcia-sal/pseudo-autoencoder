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
                candidate_length = i - dq.popleft()
                if candidate_length < min_length:
                    min_length = candidate_length

            while dq and current_sum <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if min_length == inf else min_length