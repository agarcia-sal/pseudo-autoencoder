from collections import defaultdict

def findBlackPixel(picture, target):
    if not picture or not picture[0]:
        return 0
    m, n = len(picture), len(picture[0])
    row_cnt = [0] * m
    col_cnt = [0] * n
    patterns = defaultdict(int)

    for r in range(m):
        p = ''.join(picture[r])
        patterns[p] += 1
        for c in range(n):
            if picture[r][c] == 'B':
                row_cnt[r] += 1
                col_cnt[c] += 1

    res = 0
    for r in range(m):
        p = ''.join(picture[r])
        if row_cnt[r] != target or patterns[p] != target:
            continue
        for c in range(n):
            if picture[r][c] == 'B' and col_cnt[c] == target:
                res += 1
    return res