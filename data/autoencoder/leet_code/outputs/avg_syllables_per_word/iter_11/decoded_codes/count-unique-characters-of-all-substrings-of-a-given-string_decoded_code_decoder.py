class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        last = [-1] * 26
        last2 = [-1] * 26

        result = 0

        for i, char in enumerate(s):
            idx = ord(char) - ord('A')
            result = (result + (i - last[idx]) * (last[idx] - last2[idx])) % MOD
            last2[idx] = last[idx]
            last[idx] = i

        for i in range(26):
            result = (result + (n - last[i]) * (last[i] - last2[i])) % MOD

        return result