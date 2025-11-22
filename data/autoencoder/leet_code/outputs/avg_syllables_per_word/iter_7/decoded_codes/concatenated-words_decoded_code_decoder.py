from typing import List, Optional

class Trie:
    def __init__(self) -> None:
        self.children: List[Optional[Trie]] = [None] * 26
        self.is_end: bool = False

    def insert(self, w: str) -> None:
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()

        def dfs(w: str, start: int) -> bool:
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

        ans: List[str] = []
        words.sort(key=len)
        for w in words:
            if not w:
                continue
            if dfs(w, 0):
                ans.append(w)
            else:
                trie.insert(w)
        return ans