class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def compress(word: str) -> list[tuple[str, int]]:
            if not word:
                return []
            compressed = []
            count = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    count += 1
                else:
                    compressed.append((word[i - 1], count))
                    count = 1
            compressed.append((word[-1], count))
            return compressed

        def is_stretchy(s_comp: list[tuple[str, int]], w_comp: list[tuple[str, int]]) -> bool:
            if len(s_comp) != len(w_comp):
                return False
            for (sc, sc_count), (wc, wc_count) in zip(s_comp, w_comp):
                if sc != wc:
                    return False
                if sc_count != wc_count:
                    if sc_count < 3 or sc_count < wc_count:
                        return False
            return True

        s_compressed = compress(s)
        return sum(is_stretchy(s_compressed, compress(word)) for word in words)