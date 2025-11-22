class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1

    def insert(self, word, reference_number):
        node = self
        for character in word:
            index = ord(character) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.ref = reference_number


class Solution:
    def findWords(self, board, words):
        def dfs(node, i, j):
            index = ord(board[i][j]) - ord('a')
            if node.children[index] is None:
                return
            node_ = node.children[index]
            if node_.ref >= 0:
                ans.append(words[node_.ref])
                node_.ref = -1  # avoid duplicates
            character = board[i][j]
            board[i][j] = '#'
            for a, b in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node_, x, y)
            board[i][j] = character

        tree = Trie()
        for i, w in enumerate(words):
            tree.insert(w, i)
        m, n = len(board), len(board[0]) if board else 0
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)
        return ans