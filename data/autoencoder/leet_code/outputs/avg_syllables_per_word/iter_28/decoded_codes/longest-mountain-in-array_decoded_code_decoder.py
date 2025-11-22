from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1

        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left, right = i - 1, i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                current_length = right - left + 1
                if current_length > longest:
                    longest = current_length

                i = right
            else:
                i += 1

        return longest