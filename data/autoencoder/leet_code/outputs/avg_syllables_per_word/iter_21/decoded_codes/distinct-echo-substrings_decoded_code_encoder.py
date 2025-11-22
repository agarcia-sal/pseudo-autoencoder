class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        substrings = set()

        # The outer loop iterates over possible substring lengths from 1 to n//2
        for length in range(1, n // 2 + 1):
            # The inner loop iterates over possible starting indices
            for start in range(n - 2 * length + 1):
                a = text[start:start + length]
                b = text[start + length:start + 2 * length]
                if a == b:
                    substrings.add(a + b)

        return len(substrings)