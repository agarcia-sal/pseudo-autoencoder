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
            for (char_s, count_s), (char_w, count_w) in zip(s_compressed, word_compressed):
                if char_s != char_w:
                    return False
                if count_s != count_w and (count_s < 3 or count_s < count_w):
                    return False
            return True

        s_compressed = compress(s)
        stretchy_count = 0

        for word in words:
            word_compressed = compress(word)
            if is_stretchy(s_compressed, word_compressed):
                stretchy_count += 1

        return stretchy_count