class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last = self.initializeList(26, -1)
        last2 = self.initializeList(26, -1)
        result = 0

        for i, char in enumerate(s):
            idx = self.getCharIndex(char)
            result += (i - last[idx]) * (last[idx] - last2[idx])
            result %= MOD
            last2[idx] = last[idx]
            last[idx] = i

        for i in range(26):
            result += (n - last[i]) * (last[i] - last2[i])
            result %= MOD

        return result

    @staticmethod
    def initializeList(size: int, value: int) -> list[int]:
        return [value] * size

    @staticmethod
    def getCharIndex(character: str) -> int:
        baseCharCode = ord('A')
        charCode = ord(character)
        index = charCode - baseCharCode
        return index