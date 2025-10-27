from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            it = iter(t)
            return all(c in it for c in s)

        strs.sort(key=lambda x: (-len(x), x))

        for i in range(len(strs)):
            word = strs[i]
            unique = True
            for j in range(len(strs)):
                if i != j and is_subsequence(word, strs[j]):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1