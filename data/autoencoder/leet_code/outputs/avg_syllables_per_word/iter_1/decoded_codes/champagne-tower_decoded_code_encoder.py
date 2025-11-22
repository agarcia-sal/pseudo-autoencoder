def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    row = [poured]
    for r in range(1, query_row + 1):
        nxt = [0] * (r + 1)
        for i in range(len(row)):
            if row[i] > 1:
                ex = (row[i] - 1) / 2
                nxt[i] += ex
                nxt[i + 1] += ex
        row = nxt
    return min(row[query_glass], 1)