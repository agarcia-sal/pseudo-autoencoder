class Solution:
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        m = len(image)
        n = len(image[0])

        def hasBlackPixelInRow(row):
            # Check if there is at least one '1' in the given row
            return '1' in image[row]

        def hasBlackPixelInColumn(col):
            # Check if there is at least one '1' in the given column
            for row in range(m):
                if image[row][col] == '1':
                    return True
            return False

        def findTop():
            low, high = 0, x
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInRow(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findBottom():
            low, high = x, m - 1
            while low < high:
                mid = (low + high + 1) // 2
                if hasBlackPixelInRow(mid):
                    low = mid
                else:
                    high = mid - 1
            return low

        def findLeft():
            low, high = 0, y
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInColumn(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findRight():
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

        height = bottom - top + 1
        width = right - left + 1
        area = height * width

        return area