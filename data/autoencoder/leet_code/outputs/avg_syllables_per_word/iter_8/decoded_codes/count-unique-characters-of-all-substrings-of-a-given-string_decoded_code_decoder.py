class Solution:
    def uniqueLetterString(self, s):
        MOD = 10**9 + 7
        n = len(s)
        last = [-1] * 26
        last2 = [-1] * 26
        result = 0

        for index, char in enumerate(s):
            idx = ord(char) - ord('A')
            result = (result + (index - last[idx]) * (last[idx] - last2[idx])) % MOD
            last2[idx] = last[idx]
            last[idx] = index

        for i in range(26):
            result = (result + (n - last[i]) * (last[i] - last2[i])) % MOD

        return result