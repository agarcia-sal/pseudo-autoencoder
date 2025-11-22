class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last = [-1] * 26
        last2 = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            idx = ord(char) - ord('A')
            contribution = (i - last[idx]) * (last[idx] - last2[idx])
            result = (result + contribution) % MOD
            last2[idx] = last[idx]
            last[idx] = i

        for i in range(26):
            contribution = (n - last[i]) * (last[i] - last2[i])
            result = (result + contribution) % MOD

        return result