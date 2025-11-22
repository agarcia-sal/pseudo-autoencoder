from typing import List, Tuple

class Solution:
    def getModifiedArray(self, length: int, updates: List[Tuple[int, int, int]]) -> List[int]:
        diff = [0] * (length + 1)
        for update in updates:
            startIdx, endIdx, inc = update
            diff[startIdx] += inc
            if endIdx + 1 < length:
                diff[endIdx + 1] -= inc

        arr = [0] * length
        if length == 0:
            return arr
        arr[0] = diff[0]
        for i in range(1, length):
            arr[i] = arr[i - 1] + diff[i]

        return arr