class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1,
                  1 / 9,
                  1 / 99,
                  1 / 999,
                  1 / 9999]

        def valueOf(s: str) -> float:
            leftParenIndex = s.find('(')
            if leftParenIndex == -1:
                return float(s)
            rightParenIndex = s.find(')')
            dotIndex = s.find('.')
            # Convert integer + non-repeating decimal part to float
            integerAndNonRepeating = float(s[:leftParenIndex])
            nonRepeatingLength = leftParenIndex - dotIndex - 1
            repeating = int(s[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1
            return integerAndNonRepeating + repeating * (10 ** (-nonRepeatingLength)) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9