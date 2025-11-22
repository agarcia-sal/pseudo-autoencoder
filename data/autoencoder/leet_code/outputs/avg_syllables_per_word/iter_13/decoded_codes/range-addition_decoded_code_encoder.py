class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff = [0] * (length + 1)
        for update in updates:
            startIdx, endIdx, inc = update
            diff[startIdx] += inc
            if endIdx + 1 < length:
                diff[endIdx + 1] -= inc

        arr = [0] * length
        arr[0] = diff[0]
        for i in range(1, length):
            arr[i] = arr[i - 1] + diff[i]

        return arr