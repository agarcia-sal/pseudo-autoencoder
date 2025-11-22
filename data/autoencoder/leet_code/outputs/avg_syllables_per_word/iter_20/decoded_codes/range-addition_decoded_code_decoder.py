from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)
        for startIndex, endIndex, increment in updates:
            diff[startIndex] += increment
            if endIndex + 1 < length:
                diff[endIndex + 1] -= increment

        arr = [0] * length
        if length > 0:
            arr[0] = diff[0]
        for i in range(1, length):
            arr[i] = arr[i - 1] + diff[i]
        return arr