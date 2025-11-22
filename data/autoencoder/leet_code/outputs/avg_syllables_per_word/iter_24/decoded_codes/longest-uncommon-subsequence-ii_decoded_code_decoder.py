from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            it = iter(t)
            return all(c in it for c in s)

        strs.sort(key=lambda x: (-len(x), x))

        for i, word in enumerate(strs):
            unique = True
            for j, other_word in enumerate(strs):
                if i != j and is_subsequence(word, other_word):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1