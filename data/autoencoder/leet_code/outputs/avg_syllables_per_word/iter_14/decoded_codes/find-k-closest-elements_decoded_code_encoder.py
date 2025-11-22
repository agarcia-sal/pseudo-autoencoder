import bisect
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find insertion position for x in arr to keep it sorted
        right = bisect.bisect_left(arr, x)
        left = right - 1

        # Expand the window [left+1, right) until it contains k elements
        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            else:
                if abs(arr[right] - x) < abs(arr[left] - x):
                    right += 1
                else:
                    left -= 1
        return arr[left + 1:right]