from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            # Check if s is a subsequence of t
            iter_t = iter(t)
            return all(c in iter_t for c in s)

        # Sort by descending length then lex order
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