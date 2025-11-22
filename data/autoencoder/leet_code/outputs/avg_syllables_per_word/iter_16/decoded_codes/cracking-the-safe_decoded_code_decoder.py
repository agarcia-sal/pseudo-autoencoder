class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        sequence = []

        def dfs(node: str) -> None:
            for i in range(k):
                edge = node + str(i)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    sequence.append(str(i))

        start_node = "0" * (n - 1)
        dfs(start_node)
        return "".join(sequence[::-1]) + start_node