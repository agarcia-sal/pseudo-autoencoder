from typing import List

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1

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
            node_ = node.children[idx]
            if node_.ref >= 0:
                ans.append(words[node_.ref])
                node_.ref = -1  # Avoid duplicate entries

            c = board[i][j]
            board[i][j] = '#'
            for a, b in [(-1,0), (0,1), (1,0), (0,-1)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node_, x, y)
            board[i][j] = c

        tree = Trie()
        for i, w in enumerate(words):
            tree.insert(w, i)

        m, n = len(board), len(board[0]) if board else 0
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)
        return ans