from collections import defaultdict, Counter

class Solution:
    def validArrangement(self, pairs):
        graph = defaultdict(list)
        out_degree = Counter()
        in_degree = Counter()

        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        start_node = None
        for node in graph:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        if start_node is None:
            start_node = next(iter(graph))

        path = []
        stack = [start_node]

        while stack:
            u = stack[-1]
            if graph[u]:
                v = graph[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())

        path.reverse()

        result = [[path[i], path[i+1]] for i in range(len(path)-1)]
        return result