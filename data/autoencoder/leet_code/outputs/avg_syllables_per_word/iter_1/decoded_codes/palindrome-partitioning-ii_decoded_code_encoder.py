def minCut(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if length == 2:
                is_pal[start][end] = (s[start] == s[end])
            else:
                is_pal[start][end] = (s[start] == s[end]) and is_pal[start + 1][end - 1]

    min_cut = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            min_cut[i] = 0
        else:
            min_cut[i] = float('inf')
            for j in range(1, i + 1):
                if is_pal[j][i]:
                    min_cut[i] = min(min_cut[i], min_cut[j - 1] + 1)

    return min_cut[n - 1]