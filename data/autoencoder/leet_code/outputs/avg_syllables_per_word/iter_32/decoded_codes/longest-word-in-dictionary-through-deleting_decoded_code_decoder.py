from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str, s: str) -> bool:
            it = iter(s)
            return all(char in it for char in word)

        # Sort dictionary by length descending, then lexicographically ascending
        dictionary.sort(key=lambda w: (-len(w), w))

        for word in dictionary:
            if is_subsequence(word, s):
                return word
        return ""