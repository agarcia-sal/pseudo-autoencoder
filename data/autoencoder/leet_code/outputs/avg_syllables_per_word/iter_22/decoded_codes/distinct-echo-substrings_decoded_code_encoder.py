class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        substrings = set()
        for length in range(1, n // 2 + 1):
            for start in range(n - 2 * length + 1):
                substring_a = text[start : start + length]
                substring_b = text[start + length : start + 2 * length]
                if substring_a == substring_b:
                    substrings.add(substring_a + substring_b)
        return len(substrings)