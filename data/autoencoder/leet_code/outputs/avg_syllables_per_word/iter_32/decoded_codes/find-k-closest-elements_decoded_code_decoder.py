from bisect import bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find insertion point for x in arr to maintain sorted order
        left = bisect_left(arr, x) - 1
        right = left + 1

        # Expand window [left+1, right-1] until it contains k elements
        while right - left - 1 < k:
            # If left is out of bounds (no more elements to the left),
            # or right is in bounds and right element is closer or equally close to x,
            # then move right pointer
            if left == -1 or (right < len(arr) and abs(arr[right] - x) < abs(arr[left] - x)):
                right += 1
            else:
                left -= 1

        return arr[left+1:right]