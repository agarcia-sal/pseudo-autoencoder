class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, w: str) -> None:
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()

        def dfs(w, start):
            if start == len(w):
                return True
            node = trie
            for i in range(start, len(w)):
                idx = ord(w[i]) - ord('a')
                if node.children[idx] is None:
                    return False
                node = node.children[idx]
                if node.is_end and dfs(w, i + 1):
                    return True
            return False

        ans = []
        words.sort(key=len)
        for w in words:
            if w:
                if dfs(w, 0):
                    ans.append(w)
                else:
                    trie.insert(w)
        return ans