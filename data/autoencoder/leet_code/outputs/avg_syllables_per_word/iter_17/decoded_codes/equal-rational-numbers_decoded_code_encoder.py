class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1,
                  1 / 9,
                  1 / 99,
                  1 / 999,
                  1 / 9999]

        def valueOf(s: str) -> float:
            if '(' not in s:
                return float(s)
            leftParenIndex = s.index('(')
            rightParenIndex = s.index(')')
            dotIndex = s.index('.')

            # Convert non-repeating part to float
            integerAndNonRepeating = float(s[:leftParenIndex])
            # Length of non-repeating decimal digits
            nonRepeatingLength = leftParenIndex - dotIndex - 1

            # Integer value of repeating substring
            repeating = int(s[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1

            return integerAndNonRepeating + repeating * 10**(-nonRepeatingLength) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9