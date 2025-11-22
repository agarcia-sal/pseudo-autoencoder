import bisect
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left_pointer = bisect.bisect_left(arr, x) - 1
        right_pointer = left_pointer + 1
        while right_pointer - left_pointer - 1 < k:
            if left_pointer == -1:
                right_pointer += 1
            elif right_pointer == len(arr):
                left_pointer -= 1
            else:
                if abs(arr[right_pointer] - x) < abs(arr[left_pointer] - x):
                    right_pointer += 1
                else:
                    left_pointer -= 1
        return arr[left_pointer + 1:right_pointer]