from typing import List, Optional

class Trie:
    def __init__(self):
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

        def dfs(node: Trie, i: int, j: int) -> None:
            idx = ord(board[i][j]) - ord('a')
            if node.children[idx] is None:
                return
            node = node.children[idx]
            if node.ref >= 0:
                ans.append(words[node.ref])
                node.ref = -1  # Avoid duplicate matches
            c = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited
            for a, b in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = c  # Restore the cell

        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []

        tree = Trie()
        for i, w in enumerate(words):
            if w:  # Only insert non-empty words
                tree.insert(w, i)

        ans: List[str] = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)

        return ans