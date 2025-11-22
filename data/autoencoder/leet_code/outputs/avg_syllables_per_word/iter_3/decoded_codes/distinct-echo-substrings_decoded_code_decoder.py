class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        substrings = set()

        for length in range(1, n // 2 + 1):
            for start in range(n - 2 * length + 1):
                if text[start:start+length] == text[start+length:start+2*length]:
                    substrings.add(text[start:start+2*length])

        return len(substrings)