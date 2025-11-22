class Solution:
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        m = len(image)
        n = len(image[0])

        def hasBlackPixelInRow(row):
            for pixel in image[row]:
                if pixel == '1':
                    return True
            return False

        def hasBlackPixelInColumn(col):
            for row in range(m):
                if image[row][col] == '1':
                    return True
            return False

        def findTop():
            low = 0
            high = x
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInRow(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findBottom():
            low = x
            high = m - 1
            while low < high:
                mid = (low + high + 1) // 2
                if hasBlackPixelInRow(mid):
                    low = mid
                else:
                    high = mid - 1
            return low

        def findLeft():
            low = 0
            high = y
            while low < high:
                mid = (low + high) // 2
                if hasBlackPixelInColumn(mid):
                    high = mid
                else:
                    low = mid + 1
            return low

        def findRight():
            low = y
            high = n - 1
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