class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last = [-1] * 26
        last2 = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            idx = ord(char) - ord('A')
            contribution_first = i - last[idx]
            contribution_second = last[idx] - last2[idx]
            result += contribution_first * contribution_second
            result %= MOD
            last2[idx] = last[idx]
            last[idx] = i

        for i in range(26):
            contribution_first = n - last[i]
            contribution_second = last[i] - last2[i]
            result += contribution_first * contribution_second
            result %= MOD

        return result