import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for nei, cnt in graph[node]:
                new_dist = dist + cnt + 1
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        reachable_nodes = sum(d <= maxMoves for d in distances)

        for u, v, cnt in edges:
            moves_u = max(0, maxMoves - distances[u])
            moves_v = max(0, maxMoves - distances[v])
            reachable_new_nodes = min(cnt, moves_u + moves_v)
            reachable_nodes += reachable_new_nodes

        return reachable_nodes