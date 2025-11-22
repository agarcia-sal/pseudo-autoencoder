from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            # Check if s is a subsequence of t using iterator
            it = iter(t)
            return all(c in it for c in s)

        strs.sort(key=lambda x: (-len(x), x))

        for i, word in enumerate(strs):
            unique = True
            for j, other in enumerate(strs):
                if i != j and is_subsequence(word, other):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1