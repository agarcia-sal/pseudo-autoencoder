from bisect import bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left_index = bisect_left(arr, x) - 1
        right_index = left_index + 1
        while right_index - left_index - 1 < k:
            if left_index == -1 or (right_index < len(arr) and abs(arr[right_index] - x) < abs(arr[left_index] - x)):
                right_index += 1
            else:
                left_index -= 1
        return arr[left_index + 1:right_index]