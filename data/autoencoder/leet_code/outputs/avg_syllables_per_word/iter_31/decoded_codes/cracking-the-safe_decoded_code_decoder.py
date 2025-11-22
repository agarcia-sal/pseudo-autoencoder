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

        start_node = "0" * (n - 1)
        dfs(start_node)

        reversed_sequence = sequence[::-1]
        full_sequence = "".join(reversed_sequence) + start_node
        return full_sequence