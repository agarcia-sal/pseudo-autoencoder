from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        words: List[str] = s.split()
        words.reverse()
        result: str = ' '.join(words)
        return result