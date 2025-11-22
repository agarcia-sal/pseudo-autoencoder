def generateMatrix(n):
    mat = [[0] * n for _ in range(n)]
    top, bot, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bot and left <= right:
        for i in range(left, right + 1):
            mat[top][i] = num
            num += 1
        top += 1

        for i in range(top, bot + 1):
            mat[i][right] = num
            num += 1
        right -= 1

        if top <= bot:
            for i in range(right, left - 1, -1):
                mat[bot][i] = num
                num += 1
            bot -= 1

        if left <= right:
            for i in range(bot, top - 1, -1):
                mat[i][left] = num
                num += 1
            left += 1

    return mat