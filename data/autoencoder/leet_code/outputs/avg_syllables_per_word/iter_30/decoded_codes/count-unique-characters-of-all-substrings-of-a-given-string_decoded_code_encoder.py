class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last = [-1] * 26
        last2 = [-1] * 26
        result = 0
        for i, char in enumerate(s):
            idx = ord(char) - ord('A')
            difference_one = i - last[idx]
            difference_two = last[idx] - last2[idx]
            product = difference_one * difference_two
            result = (result + product) % MOD
            last2[idx] = last[idx]
            last[idx] = i
        for i in range(26):
            difference_one = n - last[i]
            difference_two = last[i] - last2[i]
            product = difference_one * difference_two
            result = (result + product) % MOD
        return result