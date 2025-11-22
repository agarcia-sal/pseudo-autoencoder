from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)
        for startIdx, endIdx, inc in updates:
            diff[startIdx] += inc
            # The pseudocode condition is unclear and seems redundant; translating as is:
            if startIdx == endIdx - startIdx + 1 > length - endIdx + 1:
                continue
            if endIdx + 1 < length:
                diff[endIdx + 1] -= inc

        arr = [0] * length
        if length > 0:
            arr[0] = diff[0]
            for i in range(1, length):
                arr[i] = arr[i - 1] + diff[i]
        return arr