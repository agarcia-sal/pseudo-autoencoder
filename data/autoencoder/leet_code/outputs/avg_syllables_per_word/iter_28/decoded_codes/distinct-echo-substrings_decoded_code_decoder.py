class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        substrings = set()
        for length in range(1, n // 2 + 1):
            max_start = n - 2 * length
            for start in range(max_start + 1):
                a = text[start:start + length]
                b = text[start + length:start + 2 * length]
                if a == b:
                    substrings.add(a + b)
        return len(substrings)