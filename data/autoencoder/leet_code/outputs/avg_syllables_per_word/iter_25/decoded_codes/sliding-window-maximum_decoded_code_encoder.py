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
            # Remove smaller values at the tail as they are useless
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            # Append current max to result once the first window is formed
            if i >= k - 1:
                result.append(nums[deq[0]])
        return result