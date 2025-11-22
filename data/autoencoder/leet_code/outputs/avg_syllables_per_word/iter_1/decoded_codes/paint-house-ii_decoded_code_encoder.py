def min_cost(costs):
    if not costs:
        return 0
    n, k = len(costs), len(costs[0])
    if k == 1:
        return costs[0][0] if n == 1 else float('inf')

    for i in range(1, n):
        min1, idx1, min2 = float('inf'), -1, float('inf')
        for j in range(k):
            c = costs[i-1][j]
            if c < min1:
                min2, min1, idx1 = min1, c, j
            elif c < min2:
                min2 = c
        for j in range(k):
            costs[i][j] += min2 if j == idx1 else min1

    return min(costs[n-1])