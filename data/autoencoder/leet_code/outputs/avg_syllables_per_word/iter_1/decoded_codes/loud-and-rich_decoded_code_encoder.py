def loudAndRich(richer, quiet):
    n = len(quiet)
    graph = [[] for _ in range(n)]
    for a, b in richer:
        graph[b].append(a)

    answer = [-1] * n

    def dfs(p):
        if answer[p] == -1:
            answer[p] = p
            for nb in graph[p]:
                c = dfs(nb)
                if quiet[c] < quiet[answer[p]]:
                    answer[p] = c
        return answer[p]

    for i in range(n):
        dfs(i)

    return answer