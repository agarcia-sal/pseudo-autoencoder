from typing import Set, List

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited: Set[str] = set()
        sequence: List[str] = []

        def dfs(node: str) -> None:
            for i in range(k):
                edge = node + str(i)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    sequence.append(str(i))

        start_node = "0" * (n - 1) if n > 1 else ""
        dfs(start_node)
        return "".join(reversed(sequence)) + start_node