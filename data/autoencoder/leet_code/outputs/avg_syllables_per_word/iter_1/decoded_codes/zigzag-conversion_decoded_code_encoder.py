def convert(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows
    cur, down = 0, False
    for c in s:
        rows[cur] += c
        if cur == 0 or cur == numRows - 1:
            down = not down
        cur += 1 if down else -1
    return ''.join(rows)