from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements smaller than the current from the deque
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # Starting to record max values after the first full window
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result