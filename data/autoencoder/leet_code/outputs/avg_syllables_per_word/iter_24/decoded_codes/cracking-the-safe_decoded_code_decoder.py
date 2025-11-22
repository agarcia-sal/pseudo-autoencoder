class Solution:
    def crackSafe(self, n, k):
        visited = set()
        sequence = []

        def dfs(node):
            for i in range(k):
                edge = node + str(i)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    sequence.append(str(i))

        start_node = '0' * (n - 1)
        dfs(start_node)
        return ''.join(sequence) + start_node