from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1
        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
                # move left pointer to the start of the up slope
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                # move right pointer to the end of the down slope
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                length = right - left + 1
                if longest < length:
                    longest = length
                i = right
            else:
                i += 1
        return longest