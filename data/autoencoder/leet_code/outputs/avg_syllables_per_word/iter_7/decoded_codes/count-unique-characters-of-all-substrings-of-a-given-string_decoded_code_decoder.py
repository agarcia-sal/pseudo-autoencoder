from typing import List

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last: List[int] = [-1] * 26
        last2: List[int] = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            idx = ord(char) - ord('A')
            result += (i - last[idx]) * (last[idx] - last2[idx])
            result %= MOD
            last2[idx] = last[idx]
            last[idx] = i

        for i in range(26):
            result += (n - last[i]) * (last[i] - last2[i])
            result %= MOD

        return result