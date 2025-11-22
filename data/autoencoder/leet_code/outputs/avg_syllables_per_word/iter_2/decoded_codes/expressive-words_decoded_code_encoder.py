class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:

        def compress(word: str) -> list[tuple[str, int]]:
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

        def is_stretchy(s_compressed: list[tuple[str, int]], word_compressed: list[tuple[str, int]]) -> bool:
            if len(s_compressed) != len(word_compressed):
                return False
            for (sc, sc_count), (wc, wc_count) in zip(s_compressed, word_compressed):
                if sc != wc:
                    return False
                if sc_count != wc_count and (sc_count < 3 or sc_count < wc_count):
                    return False
            return True

        s_compressed = compress(s)
        stretchy_count = 0

        for word in words:
            word_compressed = compress(word)
            if is_stretchy(s_compressed, word_compressed):
                stretchy_count += 1

        return stretchy_count