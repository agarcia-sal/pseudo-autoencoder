from typing import List, Optional

class Trie:
    def __init__(self) -> None:
        self.children: List[Optional[Trie]] = [None] * 26
        self.ref: int = -1

    def insert(self, w: str, ref: int) -> None:
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = ref


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        m, n = len(board), len(board[0])
        ans: List[str] = []
        tree = Trie()
        for i, w in enumerate(words):
            tree.insert(w, i)

        # Directions: (dx, dy) pairs for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(node: Trie, i: int, j: int) -> None:
            c = board[i][j]
            idx = ord(c) - ord('a')
            next_node = node.children[idx]
            if next_node is None:
                return

            if next_node.ref >= 0:
                ans.append(words[next_node.ref])
                next_node.ref = -1  # avoid duplicates

            board[i][j] = '#'  # mark as visited

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(next_node, x, y)

            board[i][j] = c  # restore

        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)

        return ans