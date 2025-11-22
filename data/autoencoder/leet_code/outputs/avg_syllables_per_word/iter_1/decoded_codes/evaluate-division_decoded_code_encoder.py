def calcEquation(equations, values, queries):
    G = {}
    for (a,b), val in zip(equations, values):
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append((b,val))
        G[b].append((a,1/val))

    def dfs(s, e, visited):
        if s not in G or e not in G:
            return -1
        if s == e:
            return 1
        visited.add(s)
        for n, w in G[s]:
            if n not in visited:
                r = dfs(n,e,visited)
                if r != -1:
                    return w * r
        visited.remove(s)
        return -1

    results = []
    for s, e in queries:
        results.append(dfs(s, e, set()))
    return results