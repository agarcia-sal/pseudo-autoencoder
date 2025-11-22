class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1, 1 / 9, 1 / 99, 1 / 999, 1 / 9999]

        def valueOf(x: str) -> float:
            if '(' not in x:
                return float(x)
            leftParenIndex = x.index('(')
            rightParenIndex = x.index(')')
            dotIndex = x.index('.')

            integerAndNonRepeating = float(x[:leftParenIndex])
            nonRepeatingLength = leftParenIndex - dotIndex - 1
            repeating = int(x[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1

            return integerAndNonRepeating + repeating * (0.1 ** nonRepeatingLength) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9