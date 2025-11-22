from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for index in range(len(nums)):
            # Remove indices out of the current window
            if deq and deq[0] < index - k + 1:
                deq.popleft()

            # Remove smaller values at the end as they are not useful
            while deq and nums[deq[-1]] < nums[index]:
                deq.pop()

            deq.append(index)

            # Append current max to result after the first window is fully formed
            if index >= k - 1:
                result.append(nums[deq[0]])

        return result