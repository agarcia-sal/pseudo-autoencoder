from bisect import bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = bisect_left(arr, x) - 1
        right = left + 1
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