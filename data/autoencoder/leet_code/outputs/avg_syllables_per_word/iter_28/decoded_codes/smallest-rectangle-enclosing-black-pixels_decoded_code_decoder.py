from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0

        m, n = len(image), len(image[0])

        def hasBlackPixelInRow(row: int) -> bool:
            return '1' in image[row]

        def hasBlackPixelInColumn(col: int) -> bool:
            for row in range(m):
                if image[row][col] == '1':
                    return True
            return False

        def findTop() -> int:
            low, high = 0, x
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInRow(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findBottom() -> int:
            low, high = x, m - 1
            while low < high:
                mid = (low + high + 1) // 2
                if hasBlackPixelInRow(mid):
                    low = mid
                else:
                    high = mid - 1
            return low

        def findLeft() -> int:
            low, high = 0, y
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInColumn(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findRight() -> int:
            low, high = y, n - 1
            while low < high:
                mid = (low + high + 1) // 2
                if hasBlackPixelInColumn(mid):
                    low = mid
                else:
                    high = mid - 1
            return low

        top = findTop()
        bottom = findBottom()
        left = findLeft()
        right = findRight()

        return (bottom - top + 1) * (right - left + 1)