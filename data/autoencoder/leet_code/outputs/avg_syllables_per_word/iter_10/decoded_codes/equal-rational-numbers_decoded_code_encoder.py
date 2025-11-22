class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1, 1/9, 1/99, 1/999, 1/9999]

        def valueOf(num: str) -> float:
            if '(' not in num:
                return float(num)
            leftParenIndex = num.index('(')
            rightParenIndex = num.index(')')
            dotIndex = num.index('.')

            integerAndNonRepeating = float(num[:leftParenIndex])
            nonRepeatingLength = leftParenIndex - dotIndex - 1

            repeating = int(num[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1

            return integerAndNonRepeating + repeating * 10**(-nonRepeatingLength) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9