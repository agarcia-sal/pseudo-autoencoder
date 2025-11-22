def check_palindrome_partition(s):
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            is_pal[i][j] = (s[i] == s[j]) and (j - i <= 1 or is_pal[i + 1][j - 1])

    for i in range(1, n - 1):
        if is_pal[0][i - 1]:
            for j in range(i, n - 1):
                if is_pal[i][j] and is_pal[j + 1][n - 1]:
                    return True
    return False