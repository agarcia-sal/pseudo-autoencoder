def minArea(image, x, y):
    if not image or not image[0]:
        return 0
    m, n = len(image), len(image[0])

    def hasBlackInRow(r):
        return any(image[r][c] == '1' for c in range(n))

    def hasBlackInCol(c):
        return any(image[r][c] == '1' for r in range(m))

    def findTop():
        low, high = 0, x
        while low < high:
            mid = (low + high) // 2
            if hasBlackInRow(mid):
                high = mid
            else:
                low = mid + 1
        return low

    def findBottom():
        low, high = x, m - 1
        while low < high:
            mid = (low + high + 1) // 2
            if hasBlackInRow(mid):
                low = mid
            else:
                high = mid - 1
        return low

    def findLeft():
        low, high = 0, y
        while low < high:
            mid = (low + high) // 2
            if hasBlackInCol(mid):
                high = mid
            else:
                low = mid + 1
        return low

    def findRight():
        low, high = y, n - 1
        while low < high:
            mid = (low + high + 1) // 2
            if hasBlackInCol(mid):
                low = mid
            else:
                high = mid - 1
        return low

    top, bottom = findTop(), findBottom()
    left, right = findLeft(), findRight()
    return (bottom - top + 1) * (right - left + 1)