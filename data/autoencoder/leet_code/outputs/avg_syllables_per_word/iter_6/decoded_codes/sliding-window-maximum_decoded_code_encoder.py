from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for i, num in enumerate(nums):
            while deq and deq[0] < i - k + 1:
                deq.popleft()

            while deq and nums[deq[-1]] < num:
                deq.pop()

            deq.append(i)

            if i >= k - 1:
                result.append(nums[deq[0]])

        return result