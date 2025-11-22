def outerTrees(trees):
    def cross(i, j, k):
        return (trees[j][0] - trees[i][0]) * (trees[k][1] - trees[j][1]) - (trees[j][1] - trees[i][1]) * (trees[k][0] - trees[j][0])

    n = len(trees)
    if n < 4:
        return trees

    trees = sorted(trees, key=lambda x: (x[0], x[1]))
    vis = [False] * n
    stk = [0]
    vis[0] = True

    for i in range(1, n):
        while len(stk) > 1 and cross(stk[-2], stk[-1], i) < 0:
            vis[stk.pop()] = False
        vis[i] = True
        stk.append(i)

    m = len(stk)
    for i in range(n - 2, -1, -1):
        if vis[i]:
            continue
        while len(stk) > m and cross(stk[-2], stk[-1], i) < 0:
            stk.pop()
        stk.append(i)

    stk.pop()
    return [trees[i] for i in stk]