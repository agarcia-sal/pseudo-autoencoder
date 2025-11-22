from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessEqual(mid: int) -> int:
            count = 0
            row = len(matrix) - 1
            col = 0
            n = len(matrix)
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low