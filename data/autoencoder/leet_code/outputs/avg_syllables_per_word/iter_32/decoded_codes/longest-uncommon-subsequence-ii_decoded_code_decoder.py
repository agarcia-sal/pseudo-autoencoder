from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            # Check if s is a subsequence of t
            it = iter(t)
            return all(c in it for c in s)

        # Sort by descending length, then lex order ascending
        strs.sort(key=lambda x: (-len(x), x))

        n = len(strs)
        for i in range(n):
            word = strs[i]
            unique = True
            for j in range(n):
                if i == j:
                    continue
                other = strs[j]
                if is_subsequence(word, other):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1