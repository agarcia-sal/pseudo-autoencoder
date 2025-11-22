class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1

    def insert(self, w, r):
        node = self
        for c in w:
            i = ord(c) - ord('a')
            if not node.children[i]:
                node.children[i] = Trie()
            node = node.children[i]
        node.ref = r


class Solution:
    def findWords(self, board, words):
        def dfs(node, i, j):
            nonlocal ans
            i_ = ord(board[i][j]) - ord('a')
            if not node.children[i_]:
                return
            node = node.children[i_]
            if node.ref >= 0:
                ans.append(words[node.ref])
                node.ref = -1
            c, board[i][j] = board[i][j], '#'
            for a, b in [(-1,0),(0,1),(1,0),(0,-1)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = c

        tree = Trie()
        for i, w in enumerate(words):
            tree.insert(w, i)
        m, n = len(board), len(board[0])
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)
        return ans