class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1, 1/9, 1/99, 1/999, 1/9999]

        def valueOf(string_s: str) -> float:
            if '(' not in string_s:
                return float(string_s)

            leftParenIndex = string_s.index('(')
            rightParenIndex = string_s.index(')')
            dotIndex = string_s.index('.')

            integerAndNonRepeating = float(string_s[:leftParenIndex])
            nonRepeatingLength = leftParenIndex - dotIndex - 1

            repeating = int(string_s[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1

            return integerAndNonRepeating + repeating * (10 ** -nonRepeatingLength) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9