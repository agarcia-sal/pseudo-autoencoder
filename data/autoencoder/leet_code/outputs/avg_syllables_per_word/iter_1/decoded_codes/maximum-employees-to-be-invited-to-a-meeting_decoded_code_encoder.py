def maxInvitations(fav):
    n = len(fav)
    graph = {i: [] for i in range(n)}
    indeg = [0] * n
    for i in range(n):
        graph[fav[i]].append(i)
        indeg[fav[i]] += 1

    def chainLen(s, g, v):
        l = 0
        q = [s]
        v[s] = True
        while q:
            c = q.pop(0)
            for nxt in g[c]:
                if not v[nxt]:
                    v[nxt] = True
                    q.append(nxt)
                    l += 1
        return l

    def cycleLen(s, g, v, f):
        if v[s]:
            return 0
        stk = []
        c = s
        while not v[c]:
            v[c] = True
            stk.append(c)
            c = f[c]
        if c not in stk:
            return 0
        return len(stk) - stk.index(c)

    mutual_sum = 0
    visited = [False] * n
    for i in range(n):
        if fav[fav[i]] == i and i < fav[i]:
            a, b = i, fav[i]
            mutual_sum += chainLen(a, graph, visited) + chainLen(b, graph, visited)

    longest_cyc = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            longest_cyc = max(longest_cyc, cycleLen(i, graph, visited, fav))

    return max(mutual_sum, longest_cyc)