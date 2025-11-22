from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Helper function to check if s is a subsequence of t
        def is_subsequence(s: str, t: str) -> bool:
            it = iter(t)
            return all(c in it for c in s)

        # Sort strs by descending length, then lex order ascending
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