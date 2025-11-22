from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1

        while i < n - 1:
            # check if arr[i] is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1

                # expand to the left while strictly increasing
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1

                # expand to the right while strictly decreasing
                while right < n - 1 and arr[right] > arr[right+1]:
                    right += 1

                longest = max(longest, right - left + 1)
                i = right  # skip processed mountain
            else:
                i += 1

        return longest