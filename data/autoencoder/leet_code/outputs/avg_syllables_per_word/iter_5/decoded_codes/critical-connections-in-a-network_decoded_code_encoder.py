class Solution:
    def criticalConnections(self, n, connections):
        def dfs(node, parent):
            disc[node] = low[node] = time[0]
            time[0] += 1

            for neighbor in graph[node]:
                if disc[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        critical.append([node, neighbor])
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])

        def buildGraph():
            g = [[] for _ in range(n)]
            for u, v in connections:
                g[u].append(v)
                g[v].append(u)
            return g

        graph = buildGraph()
        disc = [-1] * n
        low = [-1] * n
        time = [0]
        critical = []

        for node in range(n):
            if disc[node] == -1:
                dfs(node, -1)

        return critical