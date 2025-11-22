class Solution:
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        m, n = len(image), len(image[0])

        def hasBlackPixelInRow(row):
            # Check if row contains any '1'
            return any(pixel == '1' or pixel == 1 for pixel in image[row])

        def hasBlackPixelInColumn(col):
            # Check if column contains any '1'
            for i in range(m):
                pixel = image[i][col]
                if pixel == '1' or pixel == 1:
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

        return (bottom - top + 1) * (right - left + 1)