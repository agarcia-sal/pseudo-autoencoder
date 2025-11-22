from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove indices whose corresponding values are less than nums[i]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # Append max value to result once the first window is complete
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result