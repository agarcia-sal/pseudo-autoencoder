from typing import List, Tuple

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(word: str) -> List[Tuple[str, int]]:
            if not word:
                return []
            count = 1
            compressed = []
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    count += 1
                else:
                    compressed.append((word[i - 1], count))
                    count = 1
            compressed.append((word[-1], count))
            return compressed

        def is_stretchy(s_compressed: List[Tuple[str, int]], word_compressed: List[Tuple[str, int]]) -> bool:
            if len(s_compressed) != len(word_compressed):
                return False
            for (s_char, s_count), (w_char, w_count) in zip(s_compressed, word_compressed):
                if s_char != w_char:
                    return False
                if s_count != w_count:
                    if s_count < 3 or s_count < w_count:
                        return False
            return True

        s_compressed = compress(s)
        stretchy_count = 0

        for word in words:
            word_compressed = compress(word)
            if is_stretchy(s_compressed, word_compressed):
                stretchy_count += 1

        return stretchy_count